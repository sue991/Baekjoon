from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

balloon = deque()
for i in range(N):
    balloon.append((i+1,arr[i]))

ans = []
while balloon:
    n,mov = balloon.popleft()
    ans.append(n)
    if len(balloon) == 0:
        break
    if mov > 0:
        for _ in range(mov-1):
            tmp = balloon.popleft()
            balloon.append(tmp)
    else:
        for _ in range(abs(mov)):
            tmp = balloon.pop()
            balloon.appendleft(tmp)
print(*ans)
