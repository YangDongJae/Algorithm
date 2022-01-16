in_data = list()
mul_num = 0

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i_a = 0
j = 0

for i in range (3):
    in_data.append(eval(input()))

mul_num = list(map(int, str(in_data[0] * in_data[1] * in_data[2])))

for i in mul_num:
    if i == 0:
        a += 1
    elif i == 1:
        b += 1  
    elif i == 2:
        c += 1  
    elif i == 3:
        d += 1  
    elif i == 4:
        e += 1  
    elif i == 5:
        f += 1  
    elif i == 6:
        g += 1  
    elif i == 7:
        h += 1        
    elif i == 8:
        i_a += 1                                                      
    else:
        j += 1

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i_a)
print(j)