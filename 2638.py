from collections import deque

N,M = map(int, input().split())

hours = 0
cheese = []

for _ in range(N):
    cheese.append(list(map(int, input().split())))

q = deque()
def bfs(y,x):
    visited= [[0 for _ in range(M)] for _ in range(N)]
    q.append((y,x))
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while q:
        y,x = q.popleft()
        if cheese[y][x] != 0:
            cheese[y][x] += 1
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] == 0:
                if cheese[ny][nx] == 0:
                    visited[ny][nx] = 1
                q.append((ny,nx))
    
    for i in range(N):
        for j in range(M):
            if cheese[i][j] >= 3:
                cheese[i][j] = 0
            elif cheese[i][j] == 1 or cheese[i][j] == 2:
                cheese[i][j] = 1
while True:
    for i in range(N):
        for j in range(M):
            if cheese[i][j] != 0:
                hours += 1
                bfs(0,0)
    break    
print(hours)