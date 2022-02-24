def test(word):
  for i in range (len(word)-1):
    if word[i] != word[i+1]:
      check_list = list(word[i + 2:])
      if check_list.count(word[i]):
        return False
        break

count = int(input())

return_value = 0

for i in range (count):
  
  data = input()
  if test(data) is not False:
    return_value += 1

print(return_value)
