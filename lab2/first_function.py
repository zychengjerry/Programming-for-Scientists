# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 13:10:53 2022

@author: ZeyuanCheng
"""
def odd(n):
    return 2 * n - 1

print(odd(1))
print(odd(2))
print(odd(10))


def funA(x):
    print("A", end = ' ')
    return 2*x
    
def funB(y):
    print("B", end = ' ')
    return funA(y) + 1


