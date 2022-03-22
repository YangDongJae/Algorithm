def check(num):
  check = list()
  for i in range (1, num + 1):
    result = num % i

    if result == 0:
      check.append(i)
  
  return check

a = int(input())
b = int(input())

result = list()

for i in range(a,b):
  if len(check(i)) == 2:
    result.append(check(i)[1])
  
print(result)
