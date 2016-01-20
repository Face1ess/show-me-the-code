#!/usr/bin/python
#coding=utf-8

from lxml import etree
import xlrd,codecs

def switchExcelToXML(filePath):
    try:
        excel = xlrd.open_workbook(filePath)
    except Exception,e :
        print e
    studSheet = excel.sheet_by_name('student-info')
    studDict = {}
    for row in range(0,studSheet.nrows):
        for col in range(0,studSheet.ncols):
            if col == 0 :
                studDict[studSheet.cell(row,0).value] = []
            else :
                studDict[studSheet.cell(row,0).value].append(studSheet.cell(row,col).value)
    studOutStr = '\n{\n '
    studDictKeys = sorted(studDict.keys())
    for key in studDictKeys:
        studOutStr = studOutStr + '%s : [%s, %d, %d, %d],\n ' % (key,studDict[key][0],studDict[key][1],studDict[key][2],studDict[key][3])
    studOutStr = studOutStr[:-3]+'\n}\n'

    info_students_xml = etree.ElementTree(etree.Element("root"))
    root = info_students_xml.getroot()
    students = etree.SubElement(root,"students")
    students.append(etree.Comment(u"\n\t学生信息表\n\t 'id' : [名字, 数学, 语文, 英文]\n"))
    students.text = studOutStr

    output = codecs.open('info_students.xml','w','utf-8')
    output.write(etree.tostring(info_students_xml,encoding='utf-8',pretty_print=True,xml_declaration=True).decode('utf-8'))
    output.close()
           
if __name__ == '__main__':
    switchExcelToXML('./student.xls')
    
