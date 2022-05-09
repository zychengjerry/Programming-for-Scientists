# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 16:50:10 2022

@author: ZeyuanCheng
"""
# Lab 6

import csv
with open("E:/ANU/Y2_2022_s1/COMP6730 Programming for Scientists/lab6/daily-max-temp-CBR.csv") as csvfile:
    reader = csv.reader(csvfile)
    table = [ row for row in reader ]
    
print(table[0])

col3 = [ row[3] for row in table ]

print(len(col3))

table_non_empty_col5 = [ row for row in table if row[5] != '' ]

print(len(table_non_empty_col5))

ind_non_empty_col5 = [ i for i in range(len(table)) if table[i][5] != '' ]

print(len(ind_non_empty_col5))

