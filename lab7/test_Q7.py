# -*- coding: utf-8 -*-
"""
Created on Mon May  9 16:48:03 2022

@author: ZeyuanCheng
"""
# quiz 6
a1_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(a1_list[1][1:])

print(a1_list[1][1])

print(a1_list[1:][1])

print("\n")

a_list = [-1,-3,-2]
b_list = [5, 4, 6]

a_list.sort()
print(a_list)


a_list = [-1,-3,-2]
b_list = [5, 4, 6]

a_list.extend(b_list[1:-1])
print(a_list)


a_list = [-1,-3,-2]
b_list = [5, 4, 6]

a_list.pop(0)
print(a_list)


a_list = [-1,-3,-2]
b_list = [5, 4, 6]

a_list.append(b_list[1:-1])
print(a_list)


a_list = [-1,-3,-2]
b_list = [5, 4, 6]

a_list.insert(4, 1)
print(a_list)

# a_list.remove(0)
'''
Traceback (most recent call last):

  File "E:\ANU\Y2_2022_s1\COMP6730 Programming for Scientists\lab7\test_Q6.py", line 23, in <module>
    a_list.insert(4, 1), a_list.remove(0))

ValueError: list.remove(x): x not in list
'''


def funA(alist):
    if len(alist) == 0:
        return alist
    else:
        return funA(alist[1:]) + [alist[0]]

def funB(alist):
    if len(alist) > 0:
        x = alist.pop(-1)
        alist = funB(alist)
        alist.insert(0,x)
    return alist

a = [1,2,3]
b = funB(a)
c = funA(a)
