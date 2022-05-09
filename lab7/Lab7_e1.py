# -*- coding: utf-8 -*-
"""
Created on Mon May  9 17:28:38 2022

@author: ZeyuanCheng
"""
# E 1ab
row1=["H","He"]
row2=["Li","Be","B","C","N","O","F","Ar"]
row3=["Na","Mg","Al","Si","P","S","Cl","Ne"]

ptable=row1
print(ptable)

ptable.extend(row2)
print(ptable)

ptable.extend(row3)
print(ptable)

print(id(row1))
print(id(row2))
print(id(row3))
print(id(ptable))


# E 1c
row2=["Li","Be","B","C","N","O","F","Ar"]
ptable1=["H","Xe",row2]
ptable2=ptable1[:]

print(ptable1)
print(ptable2)



# E 1d
row2=['Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ar']
ptable1=["H","Xe",row2]

import copy
ptable2=copy.deepcopy(ptable1)
print(ptable2)
