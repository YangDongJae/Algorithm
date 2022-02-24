def test(word):
  if len(word) != 1:
    pointer = word[0]
    next = word[1]

    for i in range (len(word) - 2):
      if pointer != next:
        if pointer in word[i + 2:]:
          return False
          break
      else:
        pointer = word[i + 1]
        next = word[i + 2]



count = int(input())
return_value = 0

for i in range (count):
  word = input()

  if test(word) is not False:
    return_value +=1

print(return_value)