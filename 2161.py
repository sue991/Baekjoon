from collections import deque

N = int(input())

q = deque([i for i in range(1,N+1)])
while q:
    print(q.popleft(), end=' ')
    if q:
        q.append(q.popleft())