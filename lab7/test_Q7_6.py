# -*- coding: utf-8 -*-
"""
Created on Mon May  9 17:19:16 2022

@author: ZeyuanCheng
"""

def funA( y ):
    if x >= 0:
        return y
    else:
        return -y

def funB( x ):
    return x * funA( y )

x = 1.5
y = 3
print(funB(-3))