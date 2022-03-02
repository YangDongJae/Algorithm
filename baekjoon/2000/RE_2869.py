import math
a,b,v = map(int,input().split())
day = 1 + ((v-a)/(a-b))
print(math.ceil(day))