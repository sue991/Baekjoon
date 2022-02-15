N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
cnt = [0,0,0] # -1, 0, 1

def div(x,y,n):
    global cnt
    chk = paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if chk != paper[i][j]:
                for nx in range(3):
                    for ny in range(3):
                        div(x+nx*n//3, y+ny*n//3, n//3)
                return

    # 모두 같을 경우
    cnt[chk+1] += 1

div(0,0,N)
for x in cnt:
    print(x)