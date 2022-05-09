# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 17:39:44 2022

@author: ZeyuanCheng
"""
#test
import numpy as np

table = [[2,4,4,5,6], [1,4,9], [3,6,9]]
print(table[0][2])
# for i in range(len(table)):
#     table[i] = sorted(table[i], reverse = True)


def index_ranker(l):
    temp_list = l[:]
    result = []
    temp_list.sort(reverse=True)
    for num in l:
        result.append(temp_list.index(num) + 1)
    return result

print(index_ranker(table[0]))            
print(len(table))



temp = dict()

for i in range(len(table)):
    table[i] = sorted(table[i], reverse = True)

    for j in table[i]:
        if j in temp.keys():
            temp[j] += 1
        else:
            temp[j] = 1
    
    for key, value in temp.items():
        if value > 1:
            rank_avg = np.average([key + j for j in range(value)])
            table[i] = [rank_avg if j == key else j for j in table]

print(table)