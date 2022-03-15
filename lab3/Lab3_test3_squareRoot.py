# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 16:50:34 2022

@author: ZeyuanCheng
"""
# Lab3 test3

import math

def babilun(n):
    guess_pre = 0
    guess = float(input("Guess result: "))
    tolerance = float(input("Input tolerance: "))

    while math.fabs(guess_pre - guess) > tolerance:
        guess_pre = guess
        quotient = n / guess
        guess = (quotient + guess) / 2
        
    return guess



print(babilun(23))
print(math.sqrt(23))