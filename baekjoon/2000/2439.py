num = int(input())

a = ""
b = ""

for i in range (num - 1):
    for j in range (i + 1):
        a += "*"
    for k in range (num - (i + 2)):
        b += " "

    print(b,a)
    a = ""
    b = ""
for l in range (num):
    b += "*"
print(b)