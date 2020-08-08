N,S,D = map(int, input().split())
relationship = [[] for _ in range(N)]

def dfs(x,l):
    



for _ in range(N):
    x,y = map(int, input().split())
    x -= 1 ; y -= 1
    relationship[x].append(y)
    relationship[y].append(x)