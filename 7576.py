from collections import deque

M,N = map(int, input().split())
tomato = []
q = deque()

for _ in range(N):
    tomato.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    days = 0

    while q:
        days += 1
        for _ in range(len(q)):
            y,x = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<M and 0<=ny<N:
                    if tomato[ny][nx] == 0:
                        tomato[ny][nx] = tomato[y][x] + 1
                        q.append((ny,nx))
    for x in tomato:
        if 0 in x:
            return -1
    return days-1
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            q.append((i,j))


print(bfs())