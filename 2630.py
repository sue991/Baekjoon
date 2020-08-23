N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
white, blue = 0, 0

def div(x,y,n):
    global white, blue
    chk = paper[x][y]
    tmp = n//2
    for i in range(x,x+n):
        for j in range(y,y+n):
            if chk != paper[i][j]:
                div(x,y,tmp) # 1
                div(x,y+tmp,tmp) # 2
                div(x+tmp,y,tmp) # 3
                div(x+tmp,y+tmp,tmp) # 4
                return
    if chk == 0:
        white += 1
    else:
        blue += 1
    return

if __name__ == "__main__":
    div(0,0,N)
    print(white)
    print(blue)