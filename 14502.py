from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
laboratory = [list(map(int, input().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0
def bfs(board, virus): # 세균번식
    n = 0
    visited = [[0 for _ in range(M)] for _ in range(N)]
    q = deque()
    for x in virus: q.append(x)
    while q:
        x,y = q.popleft()
        if visited[x][y] == 0:
            visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    if board[nx][ny] == 0:
                        board[nx][ny] = 2
                        q.append((nx,ny))
                    elif board[nx][ny] == 1:
                        continue
                    elif board[nx][ny] == 2:
                        q.append((nx,ny))
    for i in board:
        for j in i:
            if j == 0:  n += 1
    return n
wallss, walls, virus = [], [], [] #기존 벽, 만들 벽, 바이러스 위치
for i in range(N):
    for j in range(M):
        if laboratory[i][j] == 1:
            wallss.append((i,j))
        elif laboratory[i][j] == 2:
            virus.append((i,j))
        else:   walls.append((i,j))

for wall in combinations(walls,3):
    board = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if laboratory[i][j] == 1: board[i][j] = 1
            elif laboratory[i][j] == 2: board[i][j] = 2
    for i in range(3):  board[wall[i][0]][wall[i][1]] = 1
    ans = max(ans, bfs(board, virus))

print(ans)