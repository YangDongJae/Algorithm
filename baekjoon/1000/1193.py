# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 17:34:56 2020

@author: Mohw-IN
"""
a = eval(input())

i = 0

while a > 0:

    a -= i
    i += 1

a = i + a - 1
res = str(a) + '/' + str(i - a)

if i % 2 == 0:
    res = str(i - a ) + '/' + str(a)

print(res)