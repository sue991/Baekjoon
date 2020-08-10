import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    num = [i for i in range(n,0,-1)]
    print(*num)