from itertools import combinations
import sys
input = sys.stdin.readline

def dist(x1,y1,x2,y2): return abs(x1-x2) + abs(y1-y2)

N, M = map(int, input().split())
town = [list(map(int, input().split())) for _ in range(N)]
store = []
home = []
for i in range(N):
    for j in range(N):
        if town[i][j] == 1:
            home.append((i,j))
        elif town[i][j] == 2:
            store.append((i,j))

ans = 10000000000
for chicken in combinations(store,M):
    town_n = 0
    for x1,y1 in home:
        n = 1000000
        for x2,y2 in chicken:
            n = min(n,dist(x1,y1,x2,y2))
        town_n += n
    ans = min(ans, town_n)
print(ans)