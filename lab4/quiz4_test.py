# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 17:40:01 2022

@author: ZeyuanCheng
"""
def is_prime( n ):
    if n == 1:
        return False # 1 is not a prime
    if n == 2:
        return True # 2 is a prime
    i = 2
    while i < n:
        if (n % i) == 0:
            return False  # i divides n, so n is not prime
        else:
            return True
        i = i + 1
    return False


def count_non_zero(x):
    count = 0
    index = 0
    while index < len(x):
        index = index + 1
        if x[index] != 0:
            count = count + 1
    return count

def count_non_zero1(x):
    count = 0
    for value in x:
        if value != 0:
            count = count + 1
    return count


def count_non_zero2(x):
    count = 0
    index = len(x) - 1
    while index >= 0:
        if x[index] != 0:
            count = count + 1
        index = index - 1
    return count


def count_non_zero3(x):
    count = 0
    for value in x:
        if value != 0:
            return count + 1
    return count

print(count_non_zero3([1]))
print(count_non_zero3([0,0,0,0]))
print(count_non_zero3([-1,1,0,10,10000000]))


def add_term():
    n = 1
    total = 0.0
    while total < 5.0:
        total += 1/n
        n += 1
    return n-1

print(add_term())