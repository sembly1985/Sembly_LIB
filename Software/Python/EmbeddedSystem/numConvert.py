# -*- coding: utf-8 -*-

def value2ByteArray(value,array_len):
    retArray=[0]*array_len;
    for i in range(0,array_len):
        retArray[i]=(value>>(8*i)) & 0xff
    return retArray;        

def u32Value2ByteArray(value):
    ''' convert u32 to byte array '''
    return value2ByteArray(value,4)
    
def float2ByteArray(data):
    tmpData=abs(data);
    if(tmpData<pow(2,-127)):
        tmpData=pow(2,-127);
    elif(tmpData>pow(2,127)):
        tmpData=pow(2,127)
    index=0;
    sign=0;
    if(data<0):
        sign=1;
    while(1):
        if(tmpData>2):
            tmpData=tmpData/2;
            index=index+1;
            if(tmpData<2):
                break;
        elif(tmpData<1):
            tmpData=tmpData*2;
            index=index-1;
            if(tmpData>1):
                break;
        else:
            break;
    index=index+127;
    tail=int((tmpData-1)*pow(2,23));
    u32Value=(sign<<31) + (index<<23) + tail;
    return u32Value2ByteArray(u32Value);
    
def byteArray2Float(byte_array):
    sign=byte_array[3]>>7;
    index=((byte_array[3] & 0x7f)<<1) + (byte_array[2]>>7)-127;
    tail=byte_array[0]+(byte_array[1]<<8)+((byte_array[2] & 0x7f)<<16)
    value=(tail*1.0/pow(2,23)+1)*pow(2,index);
    if(sign==1):
        value=-value;
    return value;
    
def byteArray2Int(dataArray,ifSign):
    array_len=len(dataArray);
    ret=0;
    for i in range(0,array_len):
        ret = (ret<<8)+dataArray[array_len-i-1];
    array_max = 1<<(array_len*8-1);
    if(ifSign):
        if(ret>array_max):
            ret=ret-2*array_max;
    return ret;
    
def ub2sb(x):
    temp=x;
    if(x>=0x80):
        temp=x-0x100;
    return temp;
    
def uba2sba(x):
    return map(ub2sb,x);
    
def us2ss(x):
    temp=x;
    if(x>=0x8000):
        temp=x-0x10000;
    return temp;
    
def usa2ssa(x):
    return map(us2ss,x);
    
def ul2sl(x):
    temp=x;
    if(x>=0x80000000):
        temp=x-0x100000000;
    return temp;
    
def ula2sla(x):
    return map(ul2sl,x);