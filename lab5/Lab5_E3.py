# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 09:54:09 2022

@author: ZeyuanCheng
"""
# Lab5 E3

def count_capitals(sequence):
    count = 0
    index = 0
    while index < len(sequence):
        if 65 <= ord(sequence[index]) <= 90:
            count = count + 1
        index = index + 1
    return count

def test():
    seq = "Hello"
    seq1 = "abcde"
    seq2 = "ABCDE"
    seq3 = " "
    
    print(count_capitals(seq))
    print(count_capitals(seq1))
    print(count_capitals(seq2))
    print(count_capitals(seq3))

