sugar = int(input())

heavy = sugar // 5
light = sugar % 5

if light  % 3 == 0:
  light = light // 3
else: