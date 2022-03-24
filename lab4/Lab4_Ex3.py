# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 18:02:39 2022

@author: ZeyuanCheng
"""
# Lab4 Ex3

# Ex3.a
'''
[-1, 0, -2, 1, -3, 2] (3 negative numbers)
[i for i in range(-10, 10, 3)] (4 negative numbers)
[-1, -1, -1, -1, -1] (5 negative numbers)
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] (0 negative numbers)
'''
def count_negative(sequence):
    count = 0
    index = 0
    while index < len(sequence):
        if sequence[index] < 0:
            count = count + 1
        index = index + 1
    return count

def test():
    seq = [-1, 0, -2, 1, -3, 2]
    seq1 = [i for i in range(-10, 10, 3)]
    seq2 = [-1, -1, -1, -1, -1]
    seq3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    print(count_negative(seq))
    print(count_negative(seq1))
    print(count_negative(seq2))
    print(count_negative(seq3))


# Ex3.b
'''
for [1, 5, 9] the function should return True
for [3, 3, 4] the function should return True
for [3, 4, 2] the function should return False
'''
def is_increasing(seq):
    i = 0
    while i < len(seq)-1:
        if seq[i] <= seq[i+1]:
            i += 1
        else:
            return False
    return True

def test_is_increasing():
    seq = [1,5,9]
    seq1 = [3,3,4]
    seq2 = [3,4,2]
    
    print(is_increasing(seq))
    print(is_increasing(seq1))
    print(is_increasing(seq2))
