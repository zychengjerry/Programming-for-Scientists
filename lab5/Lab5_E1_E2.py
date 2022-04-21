# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 09:45:49 2022

@author: ZeyuanCheng
"""
# Lab5 E1
print(ord('a'), ord('A'), chr(20986)+chr(21475), ord('出'))


# Lab5 E2
aseq = "abcd"
print(type(aseq), aseq + aseq, aseq * 4, aseq[0], type(aseq[0]), aseq[1:-2])

bseq = "abdc"
print(aseq < bseq, aseq > bseq)

for elem in aseq:
    print(elem)

print(min(aseq), max(aseq), sorted(aseq), sorted(bseq))

cseq = [1,5,3,4,2]
print(type(cseq), sorted(cseq))