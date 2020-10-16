"""
Quiz : M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

Input : 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. 
(1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 
입력만 주어진다.

Output : 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
"""
import math

M,N = map(int , input().split())
z = []
value = []

for i in range (M , N + 1):
    if i == 3:
        z.append(3 % 2)
        value.append(z)
        print(3)
        z = []
    else:
        for j in range (2 , int(math.sqrt(i)) + 1):
            z.append(i % j)
        if 0 not in z:
            print(i)
        z = []

#<------- Test for check for logic to division ------->#
# M,N = map(int , input().split())

# for i in range (M , N + 1):
#     print(i , "\n")
#     for j in range (1 , i + 1):
#         print("\t",j)

#<------- Time Over Logic ------->#
# M,N = map(int , input().split())
# z = []
# value = []

# for i in range (M , N + 1):
#     for j in range (1 , i + 1):
#         if i % j == 0:
#             z.append(j)
#     value.append(z)
#     z = []

# for k in range (len(value)):
#     if len(value[k]) == 2:
#         z.append(value[k][1])

# [print(n) for n in z]
