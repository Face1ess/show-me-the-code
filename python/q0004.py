#!/usr/bin/python

def wordCount(filepath):
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
        count = len(words)
        return count
    except Exception,e:
        print e

if __name__ == '__main__':
    filepath = 'test.txt'
    count = wordCount(filepath)
    print 'The file has '+str(count)+' words.'
