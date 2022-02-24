def test(word):
  point = word[0]
  for i in range (1,len(word)):
    if word[i] != point:
      if point in word[i+1:]:
        return False
        break
  if len(word) > 1:
    test(word[1:])


count = int(input())
return_value = 0

for i in range (count):
  word = input()

  if test(word) is not False:
    return_value +=1

print(return_value)