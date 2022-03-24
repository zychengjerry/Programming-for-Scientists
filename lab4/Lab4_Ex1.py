# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 17:23:04 2022

@author: ZeyuanCheng
"""
# Lab4 Ex1

def sum_odd_digits(number):
    dsum = 0
    # only count odd digits
    '''error'''
    while number % 2 != 0:
        # add the last digit to the sum
        digit = number % 10
        dsum = dsum + digit
        # divide by 10 (rounded down) to remove the last digit
        number = number // 10
        print(number)
    return dsum

''' When the last digit is even, there will return 0 '''


def sum_even_digits(number):
    m = 1 # the position of the next digit
    dsum = 0 # the sum
    '''error'''
    while number % (10 ** m) != 0:
        # get the m:th digit
        digit = (number % (10 ** m)) // (10 ** (m - 1))
        # only add it if even:
        if digit % 2 == 0:
            dsum = dsum + digit
        m = m + 1
        print(digit)
    return dsum

''' Infinite Loop '''


def mystery(m):
    assert type(m) is int and m >= 0, "m must be a non-negative integer"
    while m > 1:
        i = 2
        while i < m:
            while m % i == 0:
                m = m // i
            i = i + 1
    return i

