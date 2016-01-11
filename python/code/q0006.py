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
           
    outputType = ['count','countDict','countRank'] 
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
    elif output == 'countRank':
        wordsDict = wordCount(filepath,'countDict')
        #wordsFilter() maybe someday implement a method to filt all those prep.
        sortedWordsList = sorted(wordsDict.items(),key=lambda wordsDict:wordsDict[1],reverse=True)
        rank = sortedWordsList[0][0]
        return rank

if __name__ == '__main__':
    filepath = 'test.txt'
    rank = wordCount(filepath,'countRank')
    print rank
    countDict = wordCount(filepath,'countDict')
    #for i in countDict :
       # print i+' : '+str(countDict[i])
