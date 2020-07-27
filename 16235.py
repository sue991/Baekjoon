import sys

N, M, K = map(int, sys.stdin.readline().split())

A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

food = [[5]*N for _ in range(N)]
trees = [[ [] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x,y,z = map(int, sys.stdin.readline().split())
    x-=1 ; y-=1
    trees[x][y].append(z)

n = 0
while(n != K):
    #Spring & Summer
    for i in range(N):
        for j in range(N):
            if len(trees[i][j]) == 0: continue
            trees[i][j].sort()
            for k in range(len(trees[i][j])):
                if trees[i][j][k] <= food[i][j]:
                    food[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1
                else:
                    die = trees[i][j][k:]
                    for x in die:
                        food[i][j] += x//2
                    trees[i][j] = trees[i][j][:k]
                    break

    #Fall
    di = [-1,-1,-1,0,0,1,1,1]
    dj = [-1,0,1,-1,1,-1,0,1]
    for i in range(N):
        for j in range(N):
            if trees[i][j]:
                for x in trees[i][j]:
                    if x%5 == 0:
                        for x in range(8):
                            ni = i + di[x]
                            nj = j + dj[x]
                            if 0 <= ni < N and 0 <= nj < N:
                                trees[ni][nj].append(1)
    #Winter
    for i in range(N):
        for j in range(N):
            food[i][j] += A[i][j]
    n+= 1

ans = 0
for i in trees:
    for j in i:
        ans += len(j)
print(ans)