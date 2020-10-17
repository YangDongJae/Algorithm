data = input().split()

a,b,c = map(int, data)
count = 0

function = a + ( b * count) < c * count

while function is False:
    count += 1
    function = a + (b * count ) < c * count
    
    if count > 100000:
        print('-1')
print(count)  
