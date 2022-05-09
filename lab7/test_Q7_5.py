# -*- coding: utf-8 -*-
"""
Created on Mon May  9 17:16:07 2022

@author: ZeyuanCheng
"""
# quiz6 Q5

def f(x):
    if y < 1:
        y = 1
    return x ** y

y = 2

print(f(2))


def f1(x):
    if y < 1:
        y = 1
    return x ** z

z = 2
print(f1(2))



def f(x):
    if y < 1:
        z = 1
        return x ** z
    else:
        return x ** y

y = 2
print(f(2))