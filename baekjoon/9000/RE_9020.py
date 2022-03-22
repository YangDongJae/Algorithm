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

    a , b = number //2 , number //2

    while True:
        if a in prime_number and b in prime_number:
            print(a,b)
            break

        else:
            a -= 1
            b += 1