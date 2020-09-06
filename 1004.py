import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x1,y1,x2,y2 = map(int, input().split())
    n = int(input())
    ans = 0
    planet = [list(map(int, input().split())) for _ in range(n)]
    for p in planet:
        if (x1-p[0])**2 + (y1-p[1])**2 < p[2]*p[2] and (x2-p[0])**2 + (y2-p[1])**2 > p[2]*p[2]:
            ans += 1
        elif (x1-p[0])**2 + (y1-p[1])**2 > p[2]*p[2] and (x2-p[0])**2 + (y2-p[1])**2 < p[2]*p[2]:
            ans += 1
    print(ans)