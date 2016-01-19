#/usr/bin/python
#coding=utf-8
import xlwt

def setXlsFromTxt(filepath):
    wb = xlwt.Workbook()
    ws = wb.add_sheet("student-info")
    try :
        f = open(filepath)
    except Exception,e :
        print e
    stuDict = eval(f.read())
    stuDictKeys = sorted(stuDict.keys())
    row = 0
    col = 0
    for key in stuDictKeys :
        ws.write(row,col,key)
        col = col+1
        for info in stuDict[key] :
            if type(info) == str :
                ws.write(row,col,info.decode('utf-8'))
            else : 
                ws.write(row,col,info)
            col = col + 1
        col = 0
        row = row+1
    wb.save('./student.xls')

if __name__ == '__main__':
    setXlsFromTxt('./student.txt')
