count = eval(input())

result = []

for i in range (count):
    a,b = map(int, input().split())
    result.append(a + b)

# for num in result[::-1]: [::-1] is reverse print method
#     print(num)

for num in result:
    print(num)