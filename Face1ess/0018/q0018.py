#!/usr/bin/python
#coding=utf-8

from lxml import etree
import xlrd,codecs

def switchExcelToXML(filePath):
    try:
        excel = xlrd.open_workbook(filePath)
    except Exception,e :
        print e
    citysSheet = excel.sheet_by_name('city')
    citysDict = {}
    for row in range(0,citysSheet.nrows):
        for col in range(0,citysSheet.ncols):
            if col == 0 :
                citysDict[citysSheet.cell(row,0).value] = ''
            else :
                citysDict[citysSheet.cell(row,0).value] = citysSheet.cell(row,col).value
    citysOutStr = '\n{\n '
    citysDictKeys = sorted(citysDict.keys())
    for key in citysDictKeys:
        citysOutStr = citysOutStr + '%s : "%s",\n ' % (key,citysDict[key])
    citysOutStr = citysOutStr[:-3]+'\n}\n'

    info_citys_xml = etree.ElementTree(etree.Element("root"))
    root = info_citys_xml.getroot()
    citys = etree.SubElement(root,"citys")
    citys.append(etree.Comment(u" 城市信息 "))
    citys.text = citysOutStr

    output = codecs.open('info_citys.xml','w','utf-8')
    output.write(etree.tostring(info_citys_xml,encoding='utf-8',pretty_print=True,xml_declaration=True).decode('utf-8'))
    output.close()
           
if __name__ == '__main__':
    switchExcelToXML('./city.xls')
    
