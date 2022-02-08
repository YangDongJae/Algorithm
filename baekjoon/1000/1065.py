

def test (num):
    rel = 0

    if num <= 99 :
        rel = num
    else:
        for i in range (100, num):
            num_list = list(map(int,str(num)))
            remote = None
            mile_stone = num_list[j] - num_list[j + 1]            
            for j in range(1, len(num_list) - 1):
                if mile_stone != num_list[j] - num_list[j+1]:
                    remote = False
                else:
                    mile_stone = num_list[j] - num_list[j+1]
                    remote = True
            if remote is True:
                rel += 1

    


                



