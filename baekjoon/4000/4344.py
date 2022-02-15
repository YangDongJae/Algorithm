def check_quiz(num):
  data = list(map(int,str(num)))
  print("data is", data, " sum value is" , num + sum(data))
  return num + sum(data)

def solve_problem(num):
    data = str(num)
    result_num = num
    for i in data:
        result_num += int(i)

    return result_num
  

factor = 1
data_list = []
check_list = [i for i in range (1,10001)]

# while factor <= 10000:
#   result_num = check_quiz(factor)
#   data_list.append(check_quiz(factor))
#   factor += 1

for i in range (1,10000):
  data_list.append(solve_problem(i))

for i in data_list:
  if i in check_list:
    check_list.remove(i)

for j in sorted(check_list):
    print(j)
