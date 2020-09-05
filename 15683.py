from collections import deque
import sys
input = sys.stdin.readline
#동,서,북,남
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def print_board(board):
    print()
    for i in board:
        for j in i:
            print(j,end=" ")
        print()
    print()

def watching(d,x,y): #각 cctvs 화긴
    w_set = set()
    for i in d:
        nx = x + dx[i]
        ny = y + dy[i]
        while 0 <= nx < N and 0 <= ny < M:
            if office[nx][ny] == 6:
                break 
            elif office[nx][ny] == 0:
                # board[nx][ny] = "#"
                w_set.add((nx,ny))
            nx += dx[i]
            ny += dy[i]
    return w_set

def dfs(n,union_set):
    global maxi
    if n == len(all_watch): 
        maxi = max(maxi,len(union_set))
        return
    for x in all_watch[n]:
        dfs(n+1,union_set|x)

if __name__ == "__main__":
    N, M = map(int, input().split())
    office = [list(map(int, input().split())) for _ in range(N)]
    cctvs = []
    watch = set()

    all_watch = []
    for i in range(N):
        for j in range(M):
            if 0 < office[i][j] < 6:   
                cctvs.append((office[i][j],i,j))
                watch.add((i,j))
            elif office[i][j] == 6:
                watch.add((i,j))

    for cctv in cctvs:
        if cctv[0] == 1:
            all_watch.append([watching([0],cctv[1],cctv[2]), watching([1],cctv[1],cctv[2]),watching([2],cctv[1],cctv[2]),watching([3],cctv[1],cctv[2])])
        elif cctv[0] == 2:
            all_watch.append([watching([0,1],cctv[1],cctv[2]), watching([2,3],cctv[1],cctv[2])])
        elif cctv[0] == 3:
            all_watch.append([watching([0,2],cctv[1],cctv[2]), watching([0,3],cctv[1],cctv[2]), watching([1,3],cctv[1],cctv[2]), watching([1,2],cctv[1],cctv[2])])
        elif cctv[0] == 4:
            all_watch.append([watching([0,1,2],cctv[1],cctv[2]), watching([0,2,3],cctv[1],cctv[2]), watching([0,1,3],cctv[1],cctv[2]), watching([1,2,3],cctv[1],cctv[2])])
        else:
            all_watch.append([watching([0,1,2,3],cctv[1],cctv[2])])

    maxi = 0
    dfs(0,watch)
    print(N*M-maxi)