from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]
cnt = 0 #단지 수
houses=[]

N = int(input())
visited = [[0 for _ in range(N)] for _ in range(N)]
apartment = []
for _ in range(N):
    tmp = [int(i) for i in input()]
    apartment.append(tmp)

def bfs(x,y):
    q = deque()
    q.append((x,y))
    num = 0
    while q:
        x,y = q.popleft()
        if visited[x][y] == 0:
            visited[x][y] = 1
            num += 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny < N:
                    if visited[nx][ny] == 0 and apartment[nx][ny] == 1:
                        q.append((nx,ny))

    return num
    
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and apartment[i][j] == 1:
            cnt += 1
            houses.append(bfs(i,j))

houses.sort()
print(cnt)
print('\n'.join(map(str,houses)))
