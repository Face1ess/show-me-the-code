#coding=utf-8
#!/usr/bin/python

def getStripedStrList(filePath):
    try:
        f = open(filePath)
        strList = f.readlines()
        for i in range(len(strList)):
             strList[i] = strList[i].strip()
        return strList
    except Exception, e:
        print e

def interactTerminal(filterPath):
    filterWords = getStripedStrList(filterPath)
    while(True):
        inStr = raw_input()
        if inStr == 'exit':
            return 0
        for i in filterWords :
            replaceStr = ''
            for j in range(len(i)):
                replaceStr = replaceStr + '*'
            inStr = inStr.replace(i,replaceStr)
        print inStr

if __name__ == '__main__':
    interactTerminal('./filtered_word.txt')
