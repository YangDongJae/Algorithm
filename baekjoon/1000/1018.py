M , N = map(int , input().split(' '))

state_list = []

#Make chess board 
for _ in range (M):
    width_list = []
    width_list.append(input())
    state_list.append(width_list)        

count = 0

for i in state_list:
    for j in i:
        prev = j[count]
        now = j[count + 1]
        print(prev , now)
