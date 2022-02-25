def test(num):
  num = num - 1
  factor = 6
  count = 1

  while num - factor > 0:
    num = num - factor
    factor += 6
    count += 1
  return count + 1

print(test(int(input())))
