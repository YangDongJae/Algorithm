x_1 , y_1 = map(int, input().split(' '))
x_2 , y_2 = map(int , input().split(' '))
x_3 , y_3 = map(int , input().split(' '))

x = [x_1 , x_2 , x_3]

y = [y_1 , y_2 , y_3]

res = []

def check(value):
    if value[0] - value[1] != 0 and value[0] - value[2] != 0:
        return value[0]
    
    elif value[1] - value[0] != 0 and value[1] - value[2] != 0:
        return value[1]

    elif value[2] - value[0] != 0 and value[2] - value[1] != 0:
        return value[2]

x = check(x)
y = check(y)

print("------------- \n" , x,y)