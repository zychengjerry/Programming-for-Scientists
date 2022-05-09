# -*- coding: utf-8 -*-
"""
Created on Mon May  9 17:35:58 2022

@author: ZeyuanCheng
"""
# Lab7_e3a

global_X = 27

def my_function(param1=123, param2="hi mom"):
    local_X = 654.321
    print("\n=== local namespace ===")  # line 1
    for name,val in list(locals().items()):
        print("name:", name, "value:", val)
    print("=======================")
    print("local_X:", local_X)
    # print("global_X:", global_X)  # line 2

my_function()

