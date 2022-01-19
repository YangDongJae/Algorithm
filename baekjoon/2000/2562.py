from operator import index


data = list()
max = 0

for i in range(9):
  data.append(eval(input()))

for i in data:
  if max < i:
     max = i

print(max)
print(data.index(max) + 1)
  