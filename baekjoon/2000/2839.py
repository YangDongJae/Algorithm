# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 17:18:06 2020

@author: Mohw-IN
"""

data = eval(input())
result = 0

if data < 3 or data > 5000:
    print ('error!')
    

    
else:
    a = data % 5
    result += data // 5
        
        
    if a > 0:
        if a == 4:
            result = -1
                
        else:
            result += 1

print(result)
                
# %3으로 나누어 떨어질 때 
# 3,5의 최소공배수값들 