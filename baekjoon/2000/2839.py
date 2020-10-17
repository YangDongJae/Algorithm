weight = eval(input())

if not weight >= 3 and weight <= 5000:
  weight = eval(input("range error please enter new weight 3 between 5000!"))

while weight % 5 < 5:
  five_package = weight // 5 
  five_package_dump = weight % 5

three_package = five_package_dump // 3


