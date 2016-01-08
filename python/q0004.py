#!/usr/bin/python

def wordCount(filepath,output):
    try : 
        f = open(filepath)
        sentences = f.read()
        sentences = sentences[:-1]#cut the last '\n'
        textFilter = {
            ',':'',
            '.':'',
            '!':'',
            '?':'',
            ':':'',
            ';':'',
            '\n':' ',
        } 
        for i in textFilter : 
            sentences = sentences.replace(i,textFilter[i]) 
        words = sentences.split(' ')
    except Exception,e :
        print e 
           
    outputType = ['count','countDict'] 
    if output not in outputType :
       print 'Usage: wordCount(filepath,[count|countDict])'
    elif output == 'count':
        count = len(words)
        return count
    elif output == 'countDict':
        countDict = {}
        for i in words :
            if i not in countDict :
                countDict[i] = 1
            else : 
                countDict[i] = countDict[i] + 1
        return countDict

if __name__ == '__main__':
    filepath = 'test.txt'
    count = wordCount(filepath,'count')
    print count
#    countDict = wordCount(filepath,'countDict')
#    for i in countDict :
#        print i+' : '+str(countDict[i])
