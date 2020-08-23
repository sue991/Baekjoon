import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

ans = 0
for x in A:
    x -= B
    ans += 1
    if x > 0:
        ans += x//C
        if x%C > 0:
            ans += 1
print(ans)