sieve = [False, False] + [True] * 9999
count = int(10000 ** 0.5)

for i in range (2, count + 1):
    if sieve[i] == True:
        for j in range (i + i , 10000, i):
            sieve[j] = False

prime_number = [i for i in range (len(sieve)) if sieve[i] == True]

for _ in range (int(input())):
    number = int(input())
    result_list = []

    for k in prime_number:
        digit = number - k
        if digit in prime_number:
            result_list.append([k, digit])

    if len(result_list) % 2 == 0:
        print(result_list[len(result_list) // 2 - 1][0],result_list[len(result_list) // 2 - 1][1])
    else:
        print(result_list[len(result_list)//2][0],result_list[len(result_list)//2][1])