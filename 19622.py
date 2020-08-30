import sys
input = sys.stdin.readline
N = int(input())
conference = [list(map(int, input().split())) for _ in range(N)]
sums = [0 for _ in range(N)]
for i in range(N):
    sums[i] = conference[i][2]
    if i == 0:  continue
    elif i == 1:
        if conference[i][0] >= conference[i-1][1]:
            sums[i] += sums[i-1]
        continue
    elif i == 2:
        if conference[i][0] >= conference[i-1][1]:
            sums[i] += sums[i-1]
        else:
            sums[i] += sums[i-2]
        continue
    if conference[i][0] < conference[i-1][1]:
        sums[i] += max(sums[i-3],sums[i-2])
    else:
        sums[i] += max(sums[i-1],sums[i-2])

print(max(sums))
    