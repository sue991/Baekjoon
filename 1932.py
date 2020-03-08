N = int(input())

rec = [list(map(int, input().split())) for i in range(N)]

for i in range(1,N):
    for j in range(len(rec[i])):
        if j == 0:
            rec[i][j] += rec[i-1][j]
        elif j == i:
            rec[i][j] += rec[i-1][j-1]

        else:
            rec[i][j] += max(rec[i-1][j-1],rec[i-1][j])

print(max(rec[N-1]))