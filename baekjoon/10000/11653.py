factor = int(input())
result = list()
def find(num):
  for i in range(2,num + 2):
    if num % i == 0:
      return i 
      
while factor / find(factor) > 1:
  result.append(find(factor))
  factor = factor / find(factor)

else:
  print(find(factor))