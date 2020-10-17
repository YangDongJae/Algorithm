# data = input().split()

# a,b,v = map(int, data)

# one_day_meter = a - b

# total_meter = v // one_day_meter

# remainder = a % v

# while 


data = input().split()

move_distance , drop_distance , total_distance = map(int, data)

day_distance = move_distance - drop_distance

remaining_distance = total_distance

for i in range(1 ,  total_distance // day_distance):
    print(i)

    if total_distance % day_distance != 0:
        print(i + 1)