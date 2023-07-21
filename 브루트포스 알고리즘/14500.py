import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x,y, cnt, total):

    if cnt == 4:
        global tmp_ans
        tmp_ans = max(total, tmp_ans)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not check[nx][ny]:

            if cnt == 2: # 2개 선택 시 (ㅗ 모양)
                check[nx][ny] = 1
                dfs(x, y, cnt+1, total+paper[nx][ny])
                check[nx][ny] = 0

            check[nx][ny] = 1
            dfs(nx, ny, cnt+1, total+paper[nx][ny])
            check[nx][ny] = 0

if __name__ == "__main__":
    n, m = map(int, input().split())
    paper = [list(map(int, input().split())) for _ in range(n)]
    check = [[0] * m for _ in range(n)]

    tmp_ans = 0
    ans = 0
    for i in range(n):
        for j in range(m):
            check[i][j] = 1
            dfs(i, j, 1, paper[i][j])
            check[i][j] = 0
            ans = max(tmp_ans, ans)

    print(ans)