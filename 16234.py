from collections import deque
import sys
input = sys.stdin.readline
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    global visited
    city = []
    population = 0
    q = deque()
    if visited[x][y] == 0: 
        q.append((x,y))
        visited[x][y] = 1
        city.append((x,y))
        population += A[x][y]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if L <= abs(A[x][y] - A[nx][ny]) <= R and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    population += A[nx][ny]
                    city.append((nx,ny))
                    q.append((nx,ny))
                else:   continue
    return city, population

if __name__ == "__main__":
    N, L, R = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    while True:
        visited = [[0 for _ in range(N)] for _ in range(N)]
        chk = 0
        for i in range(N):
            for j in range(N):
                if visited[i][j] == 0:
                    lst, p = bfs(i,j)
                    if len(lst) > 1:    chk = 1
                    div_p = p//len(lst)
                    for x,y in lst:
                        A[x][y] = div_p
        if chk: ans += 1
        else:   break
print(ans)