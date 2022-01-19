num_sub = int(input())
score = list(map(int, input().split()))

max = 0
sum_value = 0

for i in score:
  if i > max:
    max = i

for j in range (len(score)):
  score[j] = score[j]/max * 100
  sum_value += score[j]

print(sum_value / num_sub)