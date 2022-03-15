# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 17:17:09 2022

@author: ZeyuanCheng
"""
# Lab3 test4

def sum_odd_digits(n):
    s = 0
    for i in range(0, len(n)):
        if not is_even(eval(n[i])):
            s += eval(n[i])
    print("sum = {}".format(s))
    
def sum_even_digits(n):
    s = 0
    for i in range(0, len(n)):
        if is_even(eval(n[i])):
            s += eval(n[i])
    print("sum = {}".format(s))

def sum_all_digits(n):
    s = 0
    for i in range(0, len(n)):
        s += eval(n[i])
    print("sum = {}".format(s))

def is_even(x):
    if (x % 2) == 0:
        return True
    else:
        return False
    
#test
n = input("Number: ")
sum_odd_digits(n)
sum_even_digits(n)
sum_all_digits(n)