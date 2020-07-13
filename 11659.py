import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
sums = [0 for _ in range(N)]
for i in range(N):
    if i == 0:
        sums[i] = num[i]
    else:
        sums[i] = num[i] + sums[i-1]
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    if i == 1:
        print(sums[j-1])
    else:
        print(sums[j-1]-sums[i-2])