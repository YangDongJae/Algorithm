# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 10:49:21 2020

@author: Mohw-IN
"""

num = input()


def make_sum(num):
    num = ",".join(num)
    num = num.split(',')
    num = list(map(int,num))
    return num

def make_source(list_num):
    source = 0
    for i in list_num:
        source += i
    return source

for i in range (int(num) - (len(num) * 9) , int(num) + 1):
    print(i)
    print(make_sum(str(i)))
    print(make_source(make_sum(str(i))),"\n")
    
    if i + make_source(make_sum(str(i))) == int(num):
        print("----------")
        print(i)
        print("----------")
        break
    
# N = int(input())
# print_num = 0
# for i in range(1, N+1):
#     div_num = list(map(int, str(i)))
#     sum_num = i + sum(div_num)
#     if(sum_num == N):
#         print_num = i
#         break
# print(print_num)