max_value = -1

for i in range (9):
  matrix_b = list(map(int, input().split()))

  if max_value < max(matrix_b):
    max_value = max(matrix_b)
    max_location = i + 1, int(matrix_b.index(max(matrix_b)) + 1)
    
print(max_value)
print(max_location[0], max_location[1])
