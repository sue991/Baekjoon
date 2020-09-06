from collections import deque
import sys
input = sys.stdin.readline

def print_board(board):
    print()
    for i in board:
        for j in i:
            print(j,end=" ")
        print()
    print()

#동,서,북,남
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def turning(n, d):
    if (n == 2 and d == "D") or (n == 3 and d == "L"): #동쪽으로 
        return 0
    elif (n == 0 and d == "D") or (n == 1 and d == "L"): #남쪽으로
        return 3
    elif (n == 3 and d == "D") or (n == 2 and d == "L"): #서쪽으로
        return 1 
    else: #북쪽으로
        return 2

def moving(d,x,y):
    nx = x + dx[d]
    ny = y + dy[d]
    if not(0 <= nx < N and 0 <= ny < N): return -1,-1
    if (nx,ny) in snake:
        return -1,-1
    return nx,ny

if __name__ == "__main__":
    time = 0 ; snake = deque() ; d = 0 #현재 가는 방향
    snake.append((0,0))
    N = int(input())
    board = [[0 for _ in range(N)] for _ in range(N)]
    K = int(input())
    for _ in range(K):
        x,y = map(int ,input().split())
        board[x-1][y-1] = -1 #apple
    turn = deque()
    L = int(input())
    for _ in range(L):
        X,C = input().split()
        turn.append((int(X),C))

    while True:
        x,y = snake[-1][0] , snake[-1][1]
        if turn:
            if time == turn[0][0]:
                d = turning(d,turn[0][1])
                turn.popleft()
        time += 1
        nx,ny = moving(d,x,y)
        if nx == -1 and ny == -1:
            break
        else:
            snake.append((nx,ny))
        if board[nx][ny] != -1:
            snake.popleft()
        else:
            board[nx][ny] = 0
    
    print(time)