def check(num):
  check = list()
  for i in range (1, num + 1):
    result = num % i

    if result == 0:
      check.append(i)
  
  return check
  

count = int(input())

data = list(map(int,input().split()))
result = 0

for i in data:
  if len(check(i)) == 2:
    result += 1
print (result)