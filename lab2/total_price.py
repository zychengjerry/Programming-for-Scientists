# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 13:14:24 2022

@author: ZeyuanCheng
"""
def total_price(n):
    if n > 1:
        return n * 24.95 * 0.4 + 3 + (n - 1) * 0.75
    elif n == 1:
        return n * 24.95 * 0.4 + 3
    else:
        return 0