a, b = map(int, input().split())

if b - 45 < 0:
    a = a - 1
    b = 60 + b - 45
    if a < 0:
        a = 23
else:
    b = b - 45

print(a," ",b)