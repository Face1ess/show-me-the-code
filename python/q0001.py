#!/usr/bin/python
#generating 200 coupon codes 
import uuid
import random

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
        couponList.append(couponCode)
    return couponList

if __name__ == '__main__':
    couponList = generatingCouponCode(200)
    for i in couponList:
        print i 
