import sys
input = sys.stdin.readline
n = int(input())
tip = sorted([int(input()) for _ in range(n)], reverse=True)

ans = 0
for i, money in enumerate(tip):
    ans += money - i if money - i > 0 else 0

print(ans)