import sys
input = sys.stdin.readline

n = int(input())
find = int(input())

board = [[0 for _ in range(n)] for _ in range(n)]

move = []
for i in range(1, n):
    move.extend([i]*2)
move.append(n-1)

nx = [-1, 0, 1, 0] # 상 우 좌 하
ny = [0, 1, 0, -1] # 상 우 좌 하

x, y = n//2, n//2
ans = 1
board[x][y] = ans

ans_x = 0
ans_y = 0
for i,m in enumerate(move):
    for j in range(m):
        if ans == find:
            ans_x, ans_y = x,y
        ans += 1
        x += nx[i%4]
        y += ny[i%4]
        board[x][y] = ans

for row in board:
    print(*row)
print(ans_x+1, ans_y+1)