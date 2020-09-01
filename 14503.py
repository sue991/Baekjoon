import sys
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [-1,0,1,0]
ans = 0

def turning(x,y,d):
    if d == 0:
        nx = x + dx[0] ; ny = y + dy[0] ; d = 3
    elif d == 1:
        nx = x + dx[3] ; ny = y + dy[3] ; d = 0
    elif d == 2:
        nx = x + dx[2] ; ny = y + dy[2] ; d = 1
    else:
        nx = x + dx[1] ; ny = y + dy[1] ; d = 2
    return nx, ny, d
            
def back(x,y,d): # 백무빙
    if d == 0:
        nx = x + dx[1] ; ny = y + dy[1]
    elif d == 1:
        nx = x + dx[0] ; ny = y + dy[0]
    elif d == 2:
        nx = x + dx[3] ; ny = y + dy[3]
    else:
        nx = x + dx[2] ; ny = y + dy[2]
    return nx, ny, d

def cleaning(x,y):
    global ans
    if board[x][y] == 0:
        board[x][y] = 2
        ans += 1

def dfs(x,y,d):
    cleaning(x,y)
    chk = 1
    for i in range(4):
        nx,ny,d = turning(x,y,d)
        if board[nx][ny] == 0: 
            chk = 0
            break
    if chk: # 2-c,d
        nx, ny, d = back(x,y,d)
        if board[nx][ny] == 1:
            return
        else:
            dfs(nx,ny,d)
    else: # 2-a
        dfs(nx,ny,d)



if __name__ == "__main__":
    N,M = map(int, input().split())
    r,c,d = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    dfs(r,c,d)
    print(ans)