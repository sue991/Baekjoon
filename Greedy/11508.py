import sys

input = sys.stdin.readline

n = int(input())
dairy = sorted([int(input()) for _ in range(n)], reverse=True)
ans = 0

for i in range(0, n, 3):
    event = dairy[i:i+3]
    ans += sum(event) - min(event) if len(event) == 3 else sum(event)

print(ans)