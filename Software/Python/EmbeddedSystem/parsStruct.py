import re

structed_varList=[]
class VariableDef():
    def __init__(self):
        self.name=''
        self.varType=''
        self.isArray=0
        self.location=''
        self.varTypeDef=TypeDef()
    def Print(self,index):
        print('---|'*index,self.name,'**',self.location,'**',self.varTypeDef.size)
        self.varTypeDef.Print(index+1)

    def UpdateType(self,types):
        self.varTypeDef.mapId=self.varType
        self.varTypeDef.Update(types)

class TypeDef():
    def __init__(self):
        self.TypeId=''
        self.size=0
        self.location=0
        self.subElement=[]
        self.tag=''
        self.mapId=''
    def Print(self,index):
        if(len(self.subElement)>0):
            for item in self.subElement:
                item.Print(index)

    def Update(self,types):
        while(True):
            ''' step 1: search mapId in types '''
            for item in types:
                if(item.mapId==self.mapId):
                    ''' found the itme '''
                    break
            ''' check if mapId equals to typeId '''
            if(item.mapId==item.TypeId):
                ''' the item is the one '''
                self.TypeId=self.mapId
                self.size=item.size
                self.location=item.location
                self.tag=item.tag
                for ele in item.subElement:
                    self.subElement.append(ele)
                for i in range(0,len(self.subElement)):
                    self.subElement[i].UpdateType(types)
                break
            else:
                self.mapId=item.TypeId


def SearchElement(fhandle):
    items=[]
    while(True):
        tmpStr=fhandle.readline()
        r=re.search('DW_TAG_member',tmpStr)
        if(r is None):
            break
        item=VariableDef()
        tmpStr=fhandle.readline()
        if(tmpStr.count(':')>1):
            r=re.search('\): (.*)',tmpStr)
            v_n=r.group()
            item.name=str.strip(v_n[3:])
        else:
            r=re.search(': (.*)',tmpStr)
            v_n=r.group()
            item.name=str.strip(v_n[2:])

        fhandle.readline()
        fhandle.readline()

        tmpStr=fhandle.readline()
        r=re.search('<0x(.*)>\t',tmpStr)
        v_t=r.group()
        item.varType=v_t[3:-2]

        tmpStr=fhandle.readline()
        r=re.search(': (.*)\t',tmpStr)
        v_l=r.group()
        try:
            item.location=int(v_l[2:-1])
        except:
            item.location=0
        items.append(item)
    return items

def SearchUnionElements(fhandle):
    items=[]
    while(True):
        tmpStr=fhandle.readline()
        r=re.search('DW_TAG_member',tmpStr)
        if(r is None):
            break
        item=VariableDef()

        tmpStr=fhandle.readline()
        if(tmpStr.count(':')>1):
            r=re.search('\): (.*)',tmpStr)
            v_n=r.group()
            item.name=str.strip(v_n[3:])
        else:
            r=re.search(': (.*)',tmpStr)
            v_n=r.group()
            item.name=str.strip(v_n[2:])

        fhandle.readline()
        fhandle.readline()

        tmpStr=fhandle.readline()
        r=re.search('<0x(.*)>\t',tmpStr)
        v_t=r.group()
        item.varType=v_t[3:-2]

        item.location=0

        items.append(item)
    return items

def SearchTypes(filename):
    typeArray=[]
    fhandle=open(filename)
    while(True):
        tmpStr=fhandle.readline()
        if(len(tmpStr)==0):
            break
        r=re.search('<1>(.*)TAG(.*)type',tmpStr)
        #r=re.search('<1><40d3>(.*)TAG(.*)type',tmpStr)
        if(r is None):
            continue
        r=re.search('<1><.*>',tmpStr)
        id_s=r.group()
        type_id=id_s[4:-1]
        ret=TypeDef()
        ret.mapId=type_id
        r=re.search('\((.*)\)',tmpStr)
        type_name=r.group()
        if(type_name=='(DW_TAG_base_type)'):
            tmpStr=fhandle.readline()
            s=re.search(':(.*)\t',tmpStr)
            s=s.group()
            size=str.strip(s[1:])
            ret.size=int(size)
            ret.tag='base_type'
            ret.isStruct=0
            ret.TypeId=type_id
            typeArray.append(ret)
            continue
        elif(type_name=='(DW_TAG_enumeration_type)'):
            tmpStr=fhandle.readline()
            s=re.search(':(.*)\t',tmpStr)
            s=s.group()
            size=str.strip(s[1:])
            ret.size=int(size)
            ret.tag='enum_type'
            ret.isStruct=0
            ret.TypeId=type_id
            typeArray.append(ret)
            continue
        elif(type_name=='(DW_TAG_typedef)'):
            fhandle.readline()
            fhandle.readline()
            fhandle.readline()
            tmpStr=fhandle.readline()
            r=re.search('<0x(.*)>\t',tmpStr)
            if(r is None):
                ret.TypeId=''
            else:
                t_id=r.group()
                ret.TypeId=t_id[3:-2]
            ret.tag='typedef'
            typeArray.append(ret)
            continue
        elif(type_name=='(DW_TAG_volatile_type)'):
            tmpStr=fhandle.readline()
            r=re.search('<0x(.*)>\t',tmpStr)
            t_id=r.group()
            ret.TypeId=t_id[3:-2]
            ret.tag='volatile'
            typeArray.append(ret)
            continue
        elif(type_name=='(DW_TAG_array_type)'):
            tmpStr=fhandle.readline()
            r=re.search('<0x(.*)>\t',tmpStr)
            t_id=r.group()
            ret.TypeId=t_id[3:-2]
            ret.tag='array'
            ret.isArray=1
            typeArray.append(ret)
            continue
        elif(type_name=='(DW_TAG_const_type)'):
            tmpStr=fhandle.readline()
            r=re.search('<0x(.*)>\t',tmpStr)
            if(r is not None):
                t_id=r.group()
                ret.TypeId=t_id[3:-2]
                ret.tag='const'
                ret.isArray=0
                typeArray.append(ret)
            continue
        elif(type_name=='(DW_TAG_structure_type)'):
            ret.TypeId=type_id
            ret.isStruct=1
            tmpStr=fhandle.readline()
            if(tmpStr.count('DW_AT_name')>0):
                tmpStr=fhandle.readline()
            s=re.search(':(.*)\t',tmpStr)
            s=s.group()
            size=str.strip(s[1:])
            ret.size=int(size)
            ret.tag="struct"
            fhandle.readline()
            fhandle.readline()
            fhandle.readline()
            ret.subElement=SearchElement(fhandle)
            typeArray.append(ret)
            continue
        elif(type_name=='(DW_TAG_pointer_type)'):
            tmpStr=fhandle.readline()
            s=re.search(':(.*)\t',tmpStr)
            s=s.group()
            size=str.strip(s[1:])
            ret.size=int(size)

            # tmpStr=fhandle.readline()
            # r=re.search('<0x(.*)>\t',tmpStr)
            # if(r is None):
            #     print(tmpStr)
            #     exit()
            # t_id=r.group()
            #ret.TypeId=t_id[3:-2]
            ret.TypeId=type_id
            ret.tag='pointer'
            ret.isArray=0
            typeArray.append(ret)
            continue
        elif(type_name=='(DW_TAG_subroutine_type)'):
            ret.isArray=0
            ret.size=4
            ret.tag='subroutine'
            ret.TypeId=type_id
            typeArray.append(ret)
            continue
        elif(type_name=='(DW_TAG_union_type)'):
            ret.tag='union'
            ret.TypeId=type_id
            tmpStr=fhandle.readline()
            s=re.search(':(.*)\t',tmpStr)
            s=s.group()
            size=str.strip(s[1:])
            ret.size=int(size)
            fhandle.readline()
            fhandle.readline()
            fhandle.readline()
            ret.subElement=SearchUnionElements(fhandle)
            typeArray.append(ret)
            continue
    fhandle.close()
    return typeArray


def SearchVar(filename):
    vardefs=[]
    fhandle=open(filename)
    while(True):
        tmpStr=fhandle.readline()
        if(len(tmpStr)==0):
            break
        r=re.search('<1>(.*)DW_TAG_variable',tmpStr)
        if(r is not None):
            tmpStr=fhandle.readline()
            r=re.search('\): (.*)\t',tmpStr)
            if(r is None):
                continue
            tmpName=r.group()
            varName=tmpName[3:-1]

            ''' search type '''
            tmpStr=fhandle.readline()
            tmpStr=fhandle.readline()
            tmpStr=fhandle.readline()
            r=re.search('DW_AT_type',tmpStr)
            if(r is None):
                print("not match")
                continue
            r=re.search('<0x(.*)>',tmpStr)
            if(r is None):
                continue
            tmpStr=r.group()
            typeName=tmpStr[3:-1]

            tmpStr=fhandle.readline()
            r=re.search('DW_OP_addr(.*)\)',tmpStr)
            if(r is None):
                tmpStr=fhandle.readline()
                r=re.search('DW_OP_addr(.*)\)',tmpStr)
            if(r is None):
                continue
            tmpStr=r.group()
            location=int(tmpStr[12:-1],16)
            #print(varName,typeName,location)
            tmpVar=VariableDef()
            tmpVar.name=str.strip(varName)
            tmpVar.varType=typeName
            tmpVar.location=location
            tmpVar.varTypeDef=TypeDef()
            vardefs.append(tmpVar)
    fhandle.close()
    return vardefs

def SearchByName(name,varList):
    ret=VariableDef()
    flag=0
    for item in varList:
        if(item.name==name):
            flag=1
            ret=item
            break
    return flag,item

def GetNameAndArrayIndex(v):
    r=re.search('\[.*\]',v)
    if(r is None):
        return v,0
    else:
        name=v[0:(r.span()[0])]
        index=v[(r.span()[0])+1:(r.span()[1]-1)]
        return name,int(index)

def GetAddrSizeByExpression(expression):
    global structed_varList
    ''' split expression '''
    vs=expression.split('.')
    addr=0
    size=0
    targetVars=structed_varList
    for v in vs:
        name,index=GetNameAndArrayIndex(v)
        flag,v_var=SearchByName(name,targetVars)
        if(flag==0):
            print(name+" is not found")
            return -1,-1
        addr=addr+v_var.location+v_var.varTypeDef.size*index
        size=v_var.varTypeDef.size
        #print(v_var.location+v_var.varTypeDef.size*index)
        targetVars=v_var.varTypeDef.subElement
    return addr,size

def parseStructFile(srcFile):
    global structed_varList
    types=SearchTypes(srcFile)
    # print(len(types))

    structed_varList=SearchVar(srcFile)
    # print(len(vars))

    for item in structed_varList:
        item.UpdateType(types)
        #item.Print(0)

def PrintVar(varName):
    global structed_varList
    flag,v_var=SearchByName(varName,structed_varList)
    if(flag==1):
        v_var.Print(0)
    else:
        print(varName+' NOT found!')

if(__name__=='__main__'):
    srcFile=r'E:\Sembly_Wang\99_Tmp\git_work\tmp\ControllerCombine\S32KAPP\debug_woboot_all\struct.lst'
    parseStructFile(srcFile)
    print(GetAddrSizeByExpression('MOTOP_FdbCurrent.iuvw.iu'))
    print(GetAddrSizeByExpression('MOTOP_FdbCurrent.iuvw'))
    print(GetAddrSizeByExpression('MOTOP_FdbCurrent.iuvw.iv'))
    print(GetAddrSizeByExpression('Motop_Controller.refQCurrent'))
    print(GetAddrSizeByExpression('Motop_TargetVq'))
    # PrintVar('Motop_Controller')
    # PrintVar('MOTOP_FdbCurrent')
    # PrintVar('MOTOP_FdbCurrent')
    # PrintVar('MOTOP_State_Y')
    for item in structed_varList:
        print(item.name)