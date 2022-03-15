# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 13:25:13 2022

@author: ZeyuanCheng
"""
from matplotlib.pyplot import plot, show
from numpy import linspace
import math

xs = linspace(-2.0, 4.0, 60)

ys = [math.sin(x) for x in xs]

plot(xs, ys, linestyle="solid", color="blue")

show()