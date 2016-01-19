#/usr/bin/python
#coding=utf-8
import xlwt

def setXlsFromTxt(filepath):
    wb = xlwt.Workbook()
    ws = wb.add_sheet("city")
    try :
        f = open(filepath)
    except Exception,e :
        print e
    cityDict = eval(f.read())
    cityDictKeys = sorted(cityDict.keys())
    row = 0
    col = 0
    for key in cityDictKeys :
        ws.write(row,col,key)
        col = col+1
        ws.write(row,col,cityDict[key].decode('utf-8'))
        col = 0
        row = row+1
    wb.save('./city.xls')

if __name__ == '__main__':
    setXlsFromTxt('./city.txt')
