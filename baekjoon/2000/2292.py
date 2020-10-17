"""
Created on Mon Sep 21 09:21:06 2020

@author: Mohw-IN
"""
# key of result = Sum_n=1 ^ limit N_t - 1 + N_t + 6_n
import re

data = eval(input())

data_range = 2

update_data_range = 1 + 6 

result = 0
count = 1
if data < 1 or data >= 1000000000:
    print('error! please check your input data range!')

else:
    range_list = list(range(data_range , update_data_range))

    while True:
        if data == 1:
            print('0')
            break

        elif data in range_list:
            print(count)
            break

        else:
            result += 1
            data_range = update_data_range + 1
            update_data_range = (data_range + 6 * (result + 1)) - 1
            range_list = list(range(data_range , update_data_range + 1))
            print(data_range , " : " , update_data_range)
            print(range_list)
            count += 1
            print("---")

        