"""
Quiz : 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
Input : 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 
수는 1,000 이하의 자연수이다.
OutPut : 주어진 수들 중 소수의 개수를 출력한다.
"""
N = eval(input())
value_list = []
prime_number = []
count = 0

if N <= 100:
    num = input().split()
    if len(num) != N:
        print("error")
    else:
        num = list(map(int,num))
        for i in num:
            for j in range(1, i + 1):
                if i % j == 0:
                    value_list.append(j)
            prime_number.append(value_list)
            value_list = []
    for k in prime_number:
        if len(k) == 2:
            count += 1
    print(count)
 
else:
    print("error")




