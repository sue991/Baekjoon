from collections import deque

N,M = map(int, input().split())

hours = 0
cheese = []

for _ in range(N):
    cheese.append(list(map(int, input().split())))

q = deque()
def bfs(y,x):
    visited= [[0 for _ in range(M)] for _ in range(N)]
    n = 0
    q.append((y,x))
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while q:
        y,x = q.popleft()
        if visited[y][x] == 0:
            visited[y][x] = 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] == 0:
                if cheese[ny][nx] == 1:
                    cheese[ny][nx] = 0
                    n += 1
                else:
                    q.append((ny,nx))
                visited[ny][nx] = 1
    return n
                
# for x in cheese:
#     if 1 in x:
#         hours += 1
#         bfs(0,0)

bfs(0,0)
print()
for i in cheese:
    for j in i:
        print(j,end=" ")
    print()

# print(hours)


