str_charc = input()

data = list(map(str,str_charc))
check_list = [chr(i) for i in range (ord('a'), ord('z')+1)]
return_value = list()
# print(data.index('a'))

for i in check_list:
    try:
        data.index(i)
        return_value.append(data.index(i))
    except:
        return_value.append(-1)

print(*return_value)
