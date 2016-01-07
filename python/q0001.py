#!/usr/bin/python
#generating 200 coupon codes 
import uuid
import random

def generatingCouponCode(num):
    cList = []
    for i in range(0,num):
        #generating by uuid method
        cList.append(uuid.uuid1())
    return cList

if __name__ == '__main__':
    couponList = generatingCouponCode(200)
    for i in couponList:
        print i 
