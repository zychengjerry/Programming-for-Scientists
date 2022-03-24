# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 17:16:27 2022

@author: ZeyuanCheng
"""
# Lab4 Ex0

def any_one_is_sum(a,b,c):
    sum_c=a+b
    sum_b=a+c
    sum_a=b+c
    if sum_c == a+b:
        if sum_b == c+a:
            if sum_a == b+c:
                return True
    else:
        return False
    
def any_one_is_sum1(a,b,c):
    if b + c == a:
        print(True)
    if c + b == a:
        print(True)
    else:
        print(False)
    return False

# def any_one_is_sum2(a, b, c):
#     if a+b==c and a+c==b:
#         return True
#    else:
#         return False

def test():
    print(any_one_is_sum(1, 2, 3))
    print(any_one_is_sum(0, 1, 3))
    print(any_one_is_sum(0, 0, 0))
    print(any_one_is_sum(-1, 1, 0))
    
    print(any_one_is_sum1(1, 2, 3))
    print(any_one_is_sum1(0, 1, 3))
    print(any_one_is_sum1(0, 0, 0))
    print(any_one_is_sum1(-1, 1, 0))
    
'''(b) For each of the three functions above, can you work out how they are intended to work? 
That is, what was the idea of the programmer who wrote them? 
What comments would be useful to add to explain the thinking? 
Is it possible to fix them by making only a small change to each function?'''