#!/usr/bin/python
import os 
from lxml import etree

def getAllText(htmlFilePath):
    f = open(htmlFilePath)
    page = etree.HTML(f.read().lower().decode('utf-8'))
    text = page.xpath(u"//p")
    textList = []
    for i in textList :
        if i.text not in textList : 
           textList.append(i.text)
    return textList    

