from collections import deque
N = int(input())

Entrance = deque(input() for _ in range(N))
Exit = deque(input() for _ in range(N))
ans = 0
while Exit:
    now = Exit.popleft()
    if now != Entrance[0]:
        ans += 1
    Entrance.remove(now)
print(ans)