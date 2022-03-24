point = []

def check_list(point_list):
  sieve = list(set(point_list))
  
  for i in range (len(sieve)):
    num = point_list.count(sieve[i])
    
    if num == 1:
      return sieve[i]
      
for i in range(3):
  point.append(list(map(int,input().split())))

x = [i[0] for i in point]
y = [i[1] for i in point]

print(check_list(x), check_list(y))