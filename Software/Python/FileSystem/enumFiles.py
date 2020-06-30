# -*- coding: utf-8 -*-
"""
Created on Fri Jan 09 15:57:24 2015

@author: f14338b
"""
import os
def enumFiles(fold,fileType):
    '''
    enum files with ext defined in fileType
    e.g:
        enumFiles(r'C:\\Usr','.txt')
        enumFiles(r'C:\\Usr',{'.txt','.lst'})
    '''
    # check type of fileType
    if(type(fileType)==type('1')):
        fileType=[fileType]
    fileArray = list();
    curFileArray=os.listdir(fold)
    curFileArray=list(curFileArray)
    for item in curFileArray:
        tempPath = os.path.join(fold,item)
        if(os.path.isdir(tempPath)):
            subFileArray=enumFiles(tempPath,fileType)
            fileArray = fileArray.__add__(subFileArray)
        else:
            for ext in fileType:
                extArray=os.path.splitext(item)
                if(extArray[1]==ext):
                    fileArray.append(tempPath)
                #end if
            # end for
        # end if
    #end for
    return fileArray
    
def enumConditionFiles(fold,condition_fcn):
    """
    enum files with condition matched: condition_fcn(pathname)==TRUE
    
    """
    fileArray = list();
    curFileArray=os.listdir(fold)
    curFileArray=list(curFileArray)
    for item in curFileArray:
        tempPath = os.path.join(fold,item)
        if(os.path.isdir(tempPath)):
            subFileArray=enumConditionFiles(tempPath,condition_fcn)
            fileArray = fileArray.__add__(subFileArray)
        else:
            if(condition_fcn(tempPath)==True):
                fileArray.append(tempPath)
            #end if
        # end if
    #end for
    return fileArray