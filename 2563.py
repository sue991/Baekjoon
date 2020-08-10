N = int(input())
color_p = [list(map(int, input().split())) for _ in range(N)]
paper = [[0 for _ in range(101)] for _ in range(101)]
ans = 0
for x,y in color_p:
    for i in range(x,x+10):
        for j in range(y,y+10):
            paper[j][i] = 1

for i in range(101):
    for j in range(101):
        if paper[j][i] != 0:
            ans += 1
print(ans)