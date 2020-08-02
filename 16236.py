from collections import deque

def bfs(baby):
    size, a,b = baby
    fish = []
    for i in range(N):
        for j in range(N):
            if 0 < sea[i][j] < size:
                fish.append((i,j))
    dist = []
    for fx,fy in fish:
        visited = [[0 for _ in range(N)] for _ in range(N)]
        n = 0
        q = deque()
        d = 0
        q.append((d,a,b))
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        
        while q:
            dis,x,y = q.popleft()
            dis += 1

            if visited[x][y] == 0:
                visited[x][y] = 1
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < N and 0 <= ny < N:
                    if visited[nx][ny] == 0:
                        if nx == fx and ny == fy:
                            dist.append((dis,nx,ny))
                            q.clear()
                            break
                        elif sea[nx][ny] > size:
                            visited[nx][ny] = 1
                        else:
                            visited[nx][ny] = 1
                            q.append((dis,nx,ny))
    return dist

N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]
size = 2

for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            baby = (size,i,j) # 상어 위치
time = 0
mama = 1
eat = 0
while mama:
    size1, x1, y1 = baby
    feeds = bfs(baby)
    if not feeds:
        mama = 0
        break
    feeds.sort()
    d,n_x,n_y = feeds[0]
    new_size = size1
    eat += 1
    if eat == new_size:
        eat = 0
        new_size += 1
    baby = (new_size,n_x,n_y)
    sea[n_x][n_y] = 9
    sea[x1][y1] = 0
    time += d
print(time)