from sys import argv

import string
import time
import re

script, ModuleName, UserName, Folder, ModulePurpose = argv

modulename = str.lower(ModuleName)
MODULENAME = str.upper(ModuleName)

ISOTIMEFORMAT = "%Y-%m-%d %X"
create_time = time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))

def ReplaceKeywords(file):
	f_r = open(file, "r").read()
	f_r = re.sub('filename.c', file, f_r)
	f_r = re.sub('filename.h', file, f_r)
	
	FILENAME = string.upper(file)
	FILENAME = FILENAME.replace(".", "_");
	f_r = re.sub('FILENAME_H', FILENAME, f_r) 
	
	f_r = re.sub('purpose', ModulePurpose, f_r)
	f_r = re.sub('username', UserName, f_r)
	f_r = re.sub('date', create_time, f_r)
	f_w = open(file, 'wb')
	f_w.write(f_r)
	f_w.close()

if Folder == "config":
	file = modulename + "_config.c"
	ReplaceKeywords(file)
	file = modulename + "_config.h"
	ReplaceKeywords(file)

if Folder == "Dev":
	file = modulename + "_unittest.c"
	ReplaceKeywords(file)
	file = modulename + "_unittest.h"
	ReplaceKeywords(file)
	
if Folder == "PublicInt":
	file = modulename + ".h"
	ReplaceKeywords(file)
	
if Folder == "Source":
	file = modulename + ".c"
	ReplaceKeywords(file)
