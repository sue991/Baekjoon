import sys
input = sys.stdin.readline
#동,서,북,남
dx = [0,0,-1,1]
dy = [1,-1,0,0]

dice = [0,0,0,0,0,0] # 위,북,동,서,남,아래
ans = []

def rolling(x,y,d): #한번 굴려야해!
    nx = x + dx[d-1] ; ny = y + dy[d-1]
    if not(0 <= nx < N and 0 <= ny < M): return x,y
    if d == 1: #동
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif d == 2: #서
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif d == 3: #북
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    else: #남
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    copy(nx,ny)
    return nx, ny

def copy(x,y): #복사 
    if board[x][y] == 0:    board[x][y] = dice[5]
    else:   dice[5], board[x][y] = board[x][y], 0
    ans.append(dice[0])

if __name__ == "__main__":
    N,M,x,y,K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    order = list(map(int, input().split()))
    nx,ny = x,y
    for i in range(K):  nx, ny = rolling(nx,ny,order[i])    
    for x in ans:   print(x)