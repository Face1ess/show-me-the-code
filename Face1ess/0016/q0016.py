#/usr/bin/python
#coding=utf-8
import xlwt

def setXlsFromTxt(filepath):
    wb = xlwt.Workbook()
    ws = wb.add_sheet("numbers")
    try :
        f = open(filepath)
    except Exception,e :
        print e
    numLists = eval(f.read())
    row = 0
    col = 0
    for nlist in numLists :
        for num in nlist : 
            ws.write(row,col,num)
            col = col+1
        col = 0
        row = row+1
    wb.save('./numbers.xls')

if __name__ == '__main__':
    setXlsFromTxt('./numbers.txt')
