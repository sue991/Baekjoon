import sys
input = sys.stdin.readline

N = int(input())
x = [int(input()) for _ in range(N)]
if N == 1:
    print(*x)
    exit()
x.sort()
maxi = x[-1]
sums = sum(x[:-1])

if sums >= maxi:
    if (maxi%2 == 0 and sums%2 == 0) or (maxi%2 == 1 and sums%2 == 1):
        print(0)
    else:
        print(1)
else:
    print(maxi-sums)