x = list()
minimum_value = 0
c = int(input())

#-----------------buble sort-----------------#
for i in range (c):
    x.append(int(input()))

def check_value(v_list):
    for i in range(len(v_list) - 1):
        if v_list[i] - (v_list[i + 1]) * - 1 > 0:
            return False
        else:
            return True

for i in range (len(x)):
    if check_value(x) is False:
        for i in range(len(x)-1):
            if x[i] > x[i + 1]:
                minimum_value = x[i + 1]
                x[i + 1] = x[i]
                x[i] = minimum_value
print(x)

#-----------------insertation sort-----------------#

for i in range (c):
    x.append(int(input()))

def insertion_sort(arr):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
print(insertion_sort(x))