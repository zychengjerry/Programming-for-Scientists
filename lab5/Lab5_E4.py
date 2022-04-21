# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 10:00:31 2022

@author: ZeyuanCheng
"""
# Lab5 E4a

my_string = "Angry Public Swamp Methods"
L = len(my_string)

print(my_string[1:L])
print(my_string[0:L - 1])
print(my_string[0:L:2]) # from 0 to L, with 2 interive
print(my_string[11:11-6:-1])

'''print(my_string[2*L]) # string index out of range'''
print(my_string[0:2*L])


# E4b
my_list = [i + 1 for i in range(26)]
print(my_list)