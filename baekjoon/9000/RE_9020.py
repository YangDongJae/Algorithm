def test(n):
    check_list = [True] * (n + 1)
    return_list = []
    
    for i in range (2, n):
        if check_list[i] == True:
            for j in range (i + i, n, i):
                check_list[j] = False

    prime_num = [i for i in range(2,len(check_list)) if check_list[i] == True]

    for k in prime_num:
        digit = n - k

        if digit in prime_num:
            return_list.append([k, digit])

    if len(return_list) % 2 == 0:
        return return_list[len(return_list)//2 - 1]
    else:
        return return_list[len(return_list)//2]

for i in range(int(input())):
    num = int(input())

    print(test(num)[0],test(num)[1])
