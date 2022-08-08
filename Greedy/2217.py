import sys
input = sys.stdin.readline

n = int(input())
ropes = sorted([int(input()) for _ in range(n)], reverse=True)

ans = 0

for i in range(len(ropes)):
    if ropes[i] == max(ans, ropes[i]):
        ans = ropes[i]
    else:
        if ropes[i] * (i+1) > ans:
            ans = ropes[i] * (i+1)

print(ans)
