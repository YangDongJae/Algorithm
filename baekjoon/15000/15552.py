import sys

# num = int(sys.stdin.readline().split()[0])
T = int(input())

for i in range (T):
    a,b = map(int, sys.stdin.readline().split())
    print(a + b)
