data = input().split()

a,b,c = map(int, data)
count = 0

function = a + ( b * count) < c * count

if a > 0 & b > 0 & c > 0:
  while function is False:
    count += 1
    function = a + (b * count ) < c * count
  print(count)  
else:
  print('-1')
