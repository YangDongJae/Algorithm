num = eval(input())
goal = num

a = 0
b = 0
result = 0

while True:
  if num % 10 == num:
    a = 0
    b = num

  else:
    a = num // 10
    b = num % 10

  sum_num = a + b
  c = sum_num % 10

  num = b * 10 + c

  result += 1
  if num == goal:
    print(result)
    break
