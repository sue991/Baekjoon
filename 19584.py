import sys
input = sys.stdin.readline

N,M = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(N)]
road = list(map(int, input().split()) for _ in range(M))
place = [] #y값만
for x,y in p:   place.append(y)
ans = {}

for u,v,c in road:
    u -= 1 ; v -= 1
    if place[v] < place[u]:
        u,v = v,u 

    if place[u] in ans:
        ans[place[u]] += c
    else:
        ans[place[u]] = c
    
    if place[v]+1 in ans:
        ans[place[v]+1] -= c
    else:
        ans[place[v]+1] = -c

ans = sorted(ans.items())

n = 0
tmp = 0
for x,y in ans:
    tmp += y
    n = max(tmp,n)
print(n)