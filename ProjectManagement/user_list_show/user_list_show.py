import os
list_file=open('user_list.txt');
list_array=[];
while(1):
    line=list_file.readline();
    if not line:
        break;
    if(line[-1]=='\n'):
        list_array.append(line[0:-1]);
    else:
        list_array.append(line);
''' print each item in list '''
for i in range(0,len(list_array)):
    space_Index=str.find(list_array[i],' ')
    print (i, list_array[i][0:space_Index]);

while(1):
    ''' input item '''
    item=input('plsea input item, -1 to exit:');
    try:
        if(int(item)==-1):
            break
        list_item=list_array[int(item)];
        space_Index=str.find(list_item,' ')
        foldStr=list_item[space_Index+1:]
        os.startfile(foldStr);
    except:
        print('error select');