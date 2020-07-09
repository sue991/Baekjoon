from collections import deque

N,M = map(int, input().split())

relationship = [[] for _ in range(N)]
bacon, q = [], deque()

def bfs(k):
    q.append(k)
    chk = [-1 for _ in range(N)]
    chk[k] = 0
    while q:
        k = q.popleft()
        for x in relationship[k]:
            if chk[x] == -1:
                chk[x] = chk[k] + 1
                q.append(x)
    for x in chk:
        if x > 6 or x == -1:
            return False
    return True

for _ in range(M):
    A,B = map(int, input().split())
    A -= 1 ; B -= 1 
    relationship[A].append(B)
    relationship[B].append(A)

for i in range(N):
    bacon.append(bfs(i))

if False in bacon:
    print("Big World!")
else:
    print("Small World!")