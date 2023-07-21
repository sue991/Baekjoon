import sys
input = sys.stdin.readline

direction = [(1,0), (0,-1), (-1,0), (0,1)] # (x,y) 

def dragon_curve(x, y, d, g):
    board[x][y] = 1
    move = [d]
    for _ in range(g):
        temp = []
        for i in range(len(move)):
            temp.append((move[-i-1]+1)%4)
        move.extend(temp)
    for m in move:
        x += direction[m][0]
        y += direction[m][1]
        board[x][y] = 1

def dragon_curve(x, y, d, g):
    board[x][y] = 1
    move = [d]
    for _ in range(g):
        tmp = []
        for i in range(len(move), 0, -1):
            tmp.append((move[i-1]+1)%4)
        move.extend(tmp)

    for m in move:
        x += direction[m][0]
        y += direction[m][1]
        board[x][y] = 1

def count_square():
    ans = 0 
    for i in range(100):
        for j in range(100):
            if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
                ans += 1

    return ans

if __name__ == "__main__":
    n = int(input())
    board = [[0] * 101 for _ in range(101)]

    for _ in range(n):
        x, y, d, g = map(int, input().split())
        dragon_curve(x, y, d, g)
    print(count_square())