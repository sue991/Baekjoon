import sys
input = sys.stdin.readline

N = int(input())
consult = [tuple(map(int, input().split())) for _ in range(N)]

ans = [0 for _ in range(N)]

for i in range(N-1,-1,-1):
    if N-i < consult[i][0]:
        continue
    if i == N-1:
        ans[i] = consult[i][1]
        continue
    ans[i] += consult[i][1]
    if i + consult[i][0] < N:
        ans[i] += max(ans[i+consult[i][0]:])
print(max(ans))
