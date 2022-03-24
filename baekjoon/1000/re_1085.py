x,y,w,h = map(int,input().split())

sieve = []

sieve.append(w - x)
sieve.append(h - y)
sieve.append((0 - x) * -1)
sieve.append((0 - y) * -1)


print(min(sieve))