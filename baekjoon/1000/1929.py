a, b = map(int,input().split())

b += 1

sieve = [True] * b
m = int(b ** 0.5)
result_list = []

for i in range(2, m + 1):
    if sieve[i] == True:
        for j in range (i + i, b, i):
            sieve[j] = False

sieve[1] = False


for k in range (a, b):
    if sieve[k] == True:
        print(k)

# 왜 안되었는지 확인 b+= 1 하기 전에