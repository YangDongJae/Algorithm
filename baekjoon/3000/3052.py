data = [eval(input()) % 42 for i in range(10)]
count = 1
check = []

for i in data:
    if i not in check:
        check.append(i)

print(len(check))