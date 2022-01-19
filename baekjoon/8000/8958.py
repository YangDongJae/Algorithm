"""
Jan.19
I thought to solve this problem it the first "O" is a standar point and checked the previous argument of the list of the standard point.
And I think as If the previous list argument is the same "O", add the score. 
"""
def check_prev(list_data, index_i, index_j):
  return_score = 0

  while list_data[index_i][index_j - 1] == "O" and index_j != 0:
    return_score += 1
    index_j -= 1

  return return_score
    
count = int(input())
data = list()
score = 0

for i in range (count):
  data.append(input())

for i in range (len(data)):
  for j in range(len(data[i])):
    if data[i][j] == "O":
      score = check_prev(data,i,j) + 1

print(score)
  
