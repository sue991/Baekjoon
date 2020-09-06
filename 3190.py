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

def moving(d,x,y):
    pass

if __name__ == "__main__":
    time = 0 ; snake = deque((0,0))
    N = int(input())
    board = [[0 for _ in range(N)] for _ in range(N)]
    K = int(input())
    for _ in range(K):
        x,y = map(int ,input().split())
        board[x-1][y-1] = -1 #apple
    turn = []
    L = int(input())
    for _ in range(L):
        X,C = input().split()
        turn.append((int(X),C))
    print_board(board)
    print(turn)
    while True:
        
        
        break