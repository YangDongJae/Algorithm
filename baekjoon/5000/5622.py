data = [["A","B","C"],["D","E","F"],["G","H","I"],["J","K","L"],["M","N","O"],["P","Q","R","S"],["T","U","V"],["W","Y","X","Z"]]

characteristic = input()
total_score = 0

for i in characteristic:
    for j in range (len(data)):
        if i in data[j]:
            total_score += j + 3

print(total_score)
