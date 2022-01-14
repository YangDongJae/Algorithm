seq, num = map(int, input().split())
data = list(map(int, input().split()))
result = list()

for i in data:
  if i < num:
      result.append(i)
    
print(*result)