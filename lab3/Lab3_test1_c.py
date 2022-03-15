# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 16:21:50 2022

@author: ZeyuanCheng
"""
# Lab3 test1.c

def median(a, b, c):
    if a <= b <= c or c <= b <= a:
        print(b)
    elif a <= c <= b or b <= c <= a:
        print(c)
    elif b <= a <= c or c <= a <= b:
        print(a)

median(1,4,7)
median(2,3,3)
median(-5,-7,5)


def sum(a,b):
    k=b
    total=0
    while k>=a:
        total=total + 1/k
        k=k-1
    return total


#sum(0,3)
print(sum(3,0))
print(sum(1,4))


def mys(n):
    k=0
    while n>0:
        if n<10:
            return k
        n=n//10
        k=k+1
    if k>0:
        return k

print(mys(19))

x=0
if x+0:
    print("md")