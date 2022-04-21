# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 10:33:28 2022

@author: ZeyuanCheng
"""
# Lab5 E6a

def count_repetitions(string, substring):
    '''
    Count the number of repetitions of substring in string. Both
    arguments must be strings.
    '''
    n_rep = 0
    # p is the next position in the string where the substring starts
    p = string.find(substring)
    # str.find returns -1 if the substring is not found
    if p == -1:
        return n_rep
    else:
        while p >= 0:
            n_rep = n_rep + 1
            # find next position where the substring starts
            p = string[p + 1:len(string) - p].find(substring)
    return n_rep

def test1():
    print(count_repetitions("ababcccdebbfg", "ab"))
    print(count_repetitions("ababcccdebbfg", "b"))
    print(count_repetitions("ababcccdebbfg", "c"))

# test1()

# E6b

def remove_substring_everywhere(string, substring):
    '''
    Remove all occurrences of substring from string, and return
    the resulting string. Both arguments must be strings.
    '''
    p = string.find(substring)
    lsub = len(substring) # length of the substring
    while p >= 0:
        string[p : len(string) - lsub] = string[p + lsub : len(string)]
        p = string.find(substring)
    return string

def test2():
    print(remove_substring_everywhere("ababcccdebbfg", "ab"))
    print(remove_substring_everywhere("ababcccdebbfg", "b"))
    print(remove_substring_everywhere("ababcccdebbfg", "c"))

# test2()