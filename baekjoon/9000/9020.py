"""
골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 
두 소수의 합으로 나타낼 수 있다는 것이다. 이러한 수를 골드바흐 수라고 한다. 
또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다. 
예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 
14 = 3 + 11, 14 = 7 + 7이다. 10000보다 작거나 같은 모든 짝수 n에 대한 
골드바흐 파티션은 존재한다.

2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 
작성하시오. 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 
차이가 가장 작은 것을 출력한다.
"""

import math 
n = []
T = eval(input())
for num in range (T):
    n.append(eval(input()))

result_list = []

for j in range (T):
    num_list = []
    result_list = []
    a = []
    if n[j] >= 4 and n[j] <= 10000:
        num_list = list(range(2,n[j] + 1))

        if n[j] % 2 == 0:
            handler = int(math.sqrt(n[j]))

            for k in range (2,n[j]+1):
                handler = int(math.sqrt(k))

                for i in range (2 , handler + 1 ):
                    if k % i == 0:
                        num_list.remove(k)
                        break
            #print(num_list)

            for num in num_list:
                handler = n[j] - num
                #print("----\n" , n[j] , handler , num)

                if handler in num_list:
                    a = [num , handler]
                    result_list.append(a)
            print(result_list[(len(result_list)//2)][0],result_list[(len(result_list)//2)][1])