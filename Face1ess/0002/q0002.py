#!/usr/bin/python
#generating 200 coupon codes 
import uuid
import random
import MySQLdb

def generatingCouponCode(num):
    couponList = []
    ranSeed = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    for i in range(0,num):
        #generating by uuid method
        #couponList.append(uuid.uuid1())
        #generating by other method
        randn = random.sample(ranSeed,16)
        couponCode = ''
        for j in range(0,len(randn)):
            if ((j+1) % 4 == 0 and (j+1)!=len(randn)) :
               couponCode = couponCode + randn[j] + '-'
            else :
               couponCode = couponCode + randn[j]
        couponList.append((i+1,couponCode))
    return couponList

def syncCoupon2Mysql(couponList):
    try:
        conn=MySQLdb.connect(host='localhost',user='root',passwd='',db='practice',port=3307)
        cur=conn.cursor()
        cur.executemany('insert into coupon (id,coupon_code) values (%s,%s)',couponList)
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])


if __name__ == '__main__':
    couponList = generatingCouponCode(200)
    #couponList = [(1,'abcd-efgh')]
    syncCoupon2Mysql(couponList)
