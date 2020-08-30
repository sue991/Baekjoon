import sys
input = sys.stdin.readline
N = int(input())
conference = [list(map(int, input().split())) for _ in range(N)]
sums = [0 for _ in range(N)]
for i in range(N):
    if i == 0:
        sums[i] = conference[i][2]
        continue
    elif i == 1:
        sums[i] += conference[i][2]
        if conference[i][0] >= conference[i-1][1]:
            sums[i] += sums[i-1]
        continue
    sums[i] += conference[i][2]
    if conference[i][0] < conference[i-1][1]:
        sums[i] += max(sums[:i-1])
    else:
        sums[i] += max(sums[:i])

print(max(sums))
    