#!/usr/bin/python
import os
import Image

def archivePic(picPath):
    try :
        if picPath[-1] != '/':
            picPath = picPath+'/'
        picFileList = os.listdir(picPath)
        size = (1136,640)
        for i in picFileList:
            im = Image.open(picPath+i)
            im.thumbnail(size)
            im.save(picPath+i[:-4]+'tb.jpg') 
    except Exception, e:
        print e
    

if __name__ == '__main__':
        archivePic('/Users/penggarfield/Code/practice/python/trialPhotos/')
