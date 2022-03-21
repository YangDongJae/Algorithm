def test(n):

    start_n = n
    n = 2 * n + 1

    sieve = [True] * n
    count = int(n ** 0.5) + 1
    return_list = []

    for i in range(2, count):
        if sieve[i] == True:
            for j in range (i+i, n, i):
                sieve[j] = False

    for k in range (start_n + 1, len(sieve)):
        if k == 1:
            sieve[k] = False
        if sieve[k]== True:
            return_list.append(k)

    return return_list

while True:
    num = int(input())

    if num == 0:
        break

    else:
        print(len(test(num)))

