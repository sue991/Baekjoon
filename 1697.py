from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
d = [0 for _ in range(200001)]

def BFS(root):
    q = deque([root])
    while q:
        x = q.popleft()

        if x == K:
            print(d[x])
            break

        for nx in [x+1, x-1, 2*x]:
            if 0 <= nx <= 200000 and d[nx] == 0:
                d[nx] = d[x] + 1
                q.append(nx)

BFS(N)