#coding=utf-8
from lxml import etree
import urllib
import urllib2
import time

def getImgSrc(url):
    try :
        resp = urllib.urlopen(url)
        page = etree.HTML(resp.read().lower().decode('utf-8'))
        img = page.xpath(u"//img")
        imgSrcList = []
        for i in img : 
            imgSrcList.append(i.attrib['src'])
        return imgSrcList
    except Exception,e:
        print e

def downLoadImg(url,picPath):
    imgUrlList = getImgSrc(url)
    if picPath[-1] != '/':
        picPath = picPath + '/'
    filterStr = 'http://imgsrc.baidu.com/'
    for i in imgUrlList:
         if filterStr in i:
            filename = 'DSC'+time.strftime('%Y%m%d%H%M%S',time.localtime())+'.jpg'
            print '==================Start downloading=================='
            urllib.urlretrieve(i,picPath+filename)
            print '======='+picPath+filename+' download complete!======='
            time.sleep(10)

if __name__ == '__main__':
     downLoadImg('http://tieba.baidu.com/p/2166231880','./downLoadPic/')
