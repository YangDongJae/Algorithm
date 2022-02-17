def check_quiz(num):
  data = list(map(int,str(num)))
  return num + sum(data)

factor = 1
data_list = []
check_list = [i for i in range (1,10001)]

while check_quiz(factor) <= 10000:
  data_list.append(check_quiz(factor))
  factor += 1

for i in data_list:
  if i in check_list:
    check_list.remove(i)

print(len(data_list))