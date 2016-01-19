#!/usr/bin/python
#coding=utf-8

from lxml import etree
import xlrd

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
    return studDict

#if __name__ == '__main__':
    
