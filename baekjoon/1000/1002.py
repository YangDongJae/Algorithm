for _ in range (int(input())):
  x1, y1, r1, x2, y2, r2 = map(int,input().split())

  dist = ((x2 - x1)**2 + (y2 - y1)**2)** 0.5
  subtraction = (r1 - r2)**2
  summation = (r1 + r2)**2

  if x1 == x2 and y1 == y2 and r1 == r2:
    print(-1)

  elif x1 == y1 and x2 == y2 and r1 != r2:
    print(0)

  elif summation < dist or dist < subtraction:
    print(0)    

  elif subtraction < dist and subtraction < summation:
    print(2)

  elif summation == dist or subtraction == dist:
    print(1)

