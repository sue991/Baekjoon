import sys
from itertools import combinations
input = sys.stdin.readline

N,S = map(int, input().split())
num = list(map(int, input().split()))
ans = 0
for i in range(1,N+1):
    comb = combinations(num,i)
    for s in comb:
        if sum(s) == S: ans += 1
print(ans)