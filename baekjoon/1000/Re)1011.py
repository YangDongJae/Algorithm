for i in range (eval(input())):
    a , b = map(int, input.split())

    distance = b - a
    handler = 1

    while True:

        if handler ** 2 < handler <= (handler + 1 ** 2):
            break
        handler += 1

    if handler ** 2 == distance:
        print(handler - 1)
    elif handler ** 2 < handler <= handler ** 2 + handler:
        print(handler * 2)
    else:
        print((handler * 2) + 1)
        