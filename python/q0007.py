#!/usr/bin/python
import os 
import re

def countCode(codePath):
    try :
        fileList = os.listdir(codePath)
    except Exception,e:
        print e

    if  codePath[-1] != '/':
        codePath = codePath+'/'
    patternBlankLine = re.compile('^$')
    patternAnnotation = re.compile('^[#|//]')
    countDict = {'Annotation':0,'Code':0,'BlankLine':0}
    codeList = []
    for i in fileList:
        try:
            f = open(codePath+i)
        except Exception,e:
            print e
        codeList = f.readlines()
        for code in codeList:
            code = code.strip()
            if patternBlankLine.match(code):
               countDict['BlankLine'] = countDict['BlankLine']+1
            elif patternAnnotation.match(code):
               countDict['Annotation'] = countDict['Annotation']+1
            else :
               countDict['Code'] = countDict['Code']+1
    return countDict

if __name__ == '__main__':
    countDict = countCode('./code/')
    for i in countDict:
        print i+':'+str(countDict[i])
 
