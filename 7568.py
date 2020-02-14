N = int(input())

info = [[0,0] for _ in range(N)]

rank = [0 for _ in range(N)]
for i in range(N):
    info[i][0],info[i][1] = map(int, input().split())

for i in range(N):
    k = 1
    for j in range(N):
        if i == j :
            continue
        else:
            if info[i][0]<info[j][0] and info[i][1] < info[j][1]:
                k += 1
    rank[i] = k


for i in range(N):
    print(rank[i],end=" ")