while True:
  a, b, c = map(int, input().split())
  
  if a == 0 and b == 0 and c == 0:
    break

  else:
    x = [a,b,c]
    x.sort()
    if x[2] * x[2] == x[1] * x[1] + x[0] * x[0]:
      print("right")
    else:
      print("wrong")