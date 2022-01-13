num1 = eval(input())
num2 = eval(input())

if num1 > 0 and num2 > 0:
    print("1")

elif num1 > 0 and num2 < 0:
    print("4")

elif num1 < 0 and num2 > 0:
    print("2")

elif num1 < 0 and num2 < 0:
    print("3")