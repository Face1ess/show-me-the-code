#!/usr/bin/python
import os 
from lxml import etree

def getAllLink(htmlFilePath):
    f = open(htmlFilePath)
    page = etree.HTML(f.read().lower().decode('utf-8'))
    aLink = page.xpath(u"//a")
    aLinkList = []
    for i in aLink :
        if i.attrib['href'] not in aLinkList : 
           aLinkList.append(i.attrib['href'])
    return aLinkList    

