for i in range (int(input())):
  k = int(input())
  n = int(input())

  floor_list = [i for i in range (1,n+1)]
  update_list  = [0 for i in range (n)]


  if k == 1:
    print(sum(floor_list))
  else:
    for count in range (k):
      for j in range (1,n+1):
        update_list[j -1] = sum(floor_list[:j])
      floor_list = update_list
      result_list = list(update_list)
      update_list = [0 for i in range (n)]
    print(result_list[n - 1])
