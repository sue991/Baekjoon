import sys
input = sys.stdin.readline

N,M = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(N)]
road = list(map(int, input().split()) for _ in range(M))
pl = []
for x,y in p:   pl.append(y)
pl = list(set(pl))
place = {}
for i,x in enumerate(pl):
    place[x] = i
ans = [0 for _ in range(len(place)-1)]

for u,v,c in road:
    u -= 1 ; v -= 1
    if p[u][1] <= p[v][1]:
        for i in range(place[p[u][1]],place[p[v][1]]):
            ans[i] += c
    else:
        for i in range(place[p[v][1]],place[p[u][1]]):
            ans[i] += c

print(max(ans))