import sys
sys.setrecursionlimit(10**6)

T = int(input())

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):
    for i in range(4):
        mx = x+dx[i]
        my = y+dy[i]
        if 0 <= mx < M and 0 <= my < N and cabbage_field[mx][my] == 1:
            cabbage_field[mx][my] = 0
            dfs(mx,my)

for _ in range(T):
    cnt = 0

    M,N,K = map(int, input().split())
    cabbage_field = [[0 for _ in range(N)] for _ in range(M)]

    for _ in range(K):
        x,y = map(int,input().split())
        cabbage_field[x][y] = 1

    for i in range(M):
        for j in range(N):
            if cabbage_field[i][j] == 1:
                dfs(i,j)
                cnt += 1
    print(cnt)