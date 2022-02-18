a , b = input().split()

a = int(''.join(reversed(str(a))))
b = int(''.join(reversed(str(b))))

if a > b :
  print(a)
else:
  print(b)