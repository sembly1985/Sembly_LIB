import os
import sys

if(sys.version[0]=='2'):
    message = raw_input("Enter: ModuleName(one word captial) UserName(like Zhaopai.Qiu) ModulePurpose(no more than 10 words) > ")
else:
    message = input("Enter: ModuleName(one word captial) UserName(like Zhaopai.Qiu) ModulePurpose(no more than 10 words) > ")
	
string = message.split()

ModuleName = string[0]
UserName = string[1]
ModulePurpose = ""
for val in range(len(string)):
	if val == 2:
		ModulePurpose += string[val]
	if val > 2:
		ModulePurpose = ModulePurpose + " " + string[val]	

order = "ModuleCreate.bat " + ModuleName
os.system(order)

length = str(len(string))
order = "ModuleInitial.bat " + ModuleName + " " + UserName + " " + length + " " + ModulePurpose
os.system(order)

print(">> Module" + " " + ModuleName + " " + "Created.")