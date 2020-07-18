import sys
N = int(sys.stdin.readline())
An = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

sums = []
for i in range(N):
    if i == 0:
        sums.append(An[0])
    else:
        sums.append(An[i]+sums[i-1])

for _ in range(M):
    i,j = map(int, sys.stdin.readline().split())
    if i == 1:
        print(sums[j-1])
    else:
        print(sums[j-1]-sums[i-2])