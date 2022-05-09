# -*- coding: utf-8 -*-
"""
Created on Mon May  9 17:33:31 2022

@author: ZeyuanCheng
"""
# Lab7_e2

#Function 1
def make_list_of_lists1(n):
    the_list = []
    sublist = []
    while n > 0:
        the_list.append(sublist)
        sublist.append(len(sublist) + 1)
        n = n - 1
    return the_list


#Function 2
def make_list_of_lists2(n):
    the_list = []
    sublist = []
    for i in range(n):
        the_list.extend(sublist)
        sublist = sublist.insert(len(sublist), i)
    return the_list


print(make_list_of_lists1(3))

# print(make_list_of_lists2(3))
# TypeError: 'NoneType' object is not iterable
