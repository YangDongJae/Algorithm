# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 17:23:09 2020

@author: Mohw-IN
"""

for _ in range (int(input())):
    H ,W, N = map(int,input().split())
    a = N%H; b = N//H + 1

    if a == 0: a = h ; b -= 1
    print(a * 100 + b)
    
    



    