import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))

P = sorted(P)
cnt = 0
for x in P:
    cnt = cnt + x*N
    N-=1

print(cnt)