count = int(input())

for i in range (count):
  h, w, n = map(int,input().split())
  floor = n % h
  test = (n // h) + 1

  if floor == 0:
    floor = h
    test -= 1

  if test < 10:
    test = "0" + str(test)
    print(floor,test, sep = "")
  else:
    print(floor,test, sep = "")