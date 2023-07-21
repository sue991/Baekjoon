import sys
input = sys.stdin.readline

direction = [(0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)]

def move_cloud(d, s):
    global cloud
    for i in range(len(cloud)):
        cloud[i] = ((cloud[i][0] + direction[d-1][0]*s) % N, (cloud[i][1] + direction[d-1][1]*s) % N)
        
def rain():
    global cloud
    for i in range(len(cloud)):
        A[cloud[i][0]][cloud[i][1]] += 1
        visited[cloud[i][0]][cloud[i][1]] = 1
    
def copy_water():
    global cloud
    diagonal = [(1,1), (1,-1), (-1,1), (-1,-1)]
    for i in range(len(cloud)):
        x, y = cloud[i][0], cloud[i][1]
        cnt = 0
        for dig in diagonal:
            nx, ny = x + dig[0], y + dig[1]
            if 0 <= nx < N and 0 <= ny < N and A[nx][ny] > 0:
                cnt += 1
        A[x][y] += cnt

def make_cloud():
    global cloud
    new_cloud = []
    for i in range(N):
        for j in range(N):
            if A[i][j] >= 2 and visited[i][j] == 0:
                new_cloud.append((i,j))
                A[i][j] -= 2
    
    cloud = new_cloud


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    move = [list(map(int, input().split())) for _ in range(M)]

    cloud = [(N-1,0), (N-1,1), (N-2,0), (N-2,1)]
    visited = [[0]*N for _ in range(N)]


    for d, s in move:
        move_cloud(d, s)
        rain()
        copy_water()
        make_cloud()
        visited = [[0]*N for _ in range(N)]
    print(sum(sum(A,[])))
