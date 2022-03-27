# num = int(input())
# if num == 0:
#   print(1)
# else:
#   x = num
#   for i in range (num - 1, 1, -1):
#     x *= i

#   print(x)




def test(n):
  if n != 2:
    print(n)
    n = n - 1
    test(n)