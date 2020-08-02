from collections import deque
import sys

dx = [1,-1,0,0]
dy = [0,0,1,-1]

R,C,T = map(int, sys.stdin.readline().split())
ans = 0

A = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
air_cleaner = []

for i in range(R): 
    if A[i][0] == -1:
        air_cleaner.append((i,0))
        air_cleaner.append((i+1,0))
        break

def DOF(): #diffusion of fine dust 
    diffusion = [[0 for _ in range(C)] for _ in range (R)]
    dust = deque()
    for i in range(R):
        for j in range(C):
            if A[i][j] > 0:
                m = A[i][j]
                dust.append((m,i,j))
    while dust:
        m,x,y = dust.popleft()
        aod = m//5
        n = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and A[nx][ny] != -1:
                n += 1
                diffusion[nx][ny] += aod
        A[x][y] = m - aod*n

    for i in range(R):
        for j in range(C):
            A[i][j] += diffusion[i][j]

def refresh(x): #미세먼지 안녕!
    if x == 0:
        a,b = air_cleaner[0]
        tmp = A[0][0]
        A[0] = A[0][1:]+[0]
        for i in range(a-1,0,-1):
            if i == 1:
                A[i][0] = tmp
            else:
                A[i][0] = A[i-1][0]
        tmp2 = A[a][-1]
        A[a] = [-1,0] + A[a][1:-1]
        for i in range(a):
            if i == a-1:
                A[i][-1] = tmp2
            else:
                A[i][-1] = A[i+1][-1]
    else:
        a,b = air_cleaner[1]
        tmp = A[-1][0]
        A[-1] = A[-1][1:]+[0]
        for i in range(a+1,R-1):
            if i == R-2:
                A[i][0] = tmp
            else:
                A[i][0] = A[i+1][0]
        tmp2 = A[a][-1]
        A[a] = [-1,0] + A[a][1:-1]
        for i in range(R-1,a,-1):
            if i == a+1:
                A[i][-1] = tmp2
            else:
                A[i][-1] = A[i-1][-1]

while(T>0):
    DOF()
    refresh(0)
    refresh(1)
    T-=1

for i in A:
    for j in i:
        if j > 0:
            ans += j
print(ans)