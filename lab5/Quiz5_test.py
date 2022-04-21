# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 15:27:24 2022

@author: ZeyuanCheng
"""
# Quiz5 test

# 86,101,114,121,32,72,97,114,100,32,69,120,97,109

def q1():
    seq = [86,101,114,121,32,72,97,114,100,32,69,120,97,109]
    seq1 = [86,101,114,121,32,72,97,114,100,32,69,120,97,109]
    for i in range(len(seq)):
        seq1[i] = chr(seq[i])
    print(seq1)
    
q1()


s = "problem"

print(s[1:4])
print(s[0:len(s):-1])
print(s[-1:len(s)])
print(s[-len(s)])


def f(s):
    for elem1 in s:
        for elem2 in s[::-1]:
            if elem1 == elem2:
                return elem1
            
print(f("abcbdc"))

