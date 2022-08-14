"""
mod_i : A_0...i 합의 % m
mod_cnt : 각 나머지 개수
동일한 나머지 개수에서 2개를 뽑은 구간의 합은 m으로 나누어떨어짐
mod_cnt Combination_2 = mod_cnt[i] * (mod_cnt[i]-1) //2

"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))

mod = [0 for _ in range(n)]

sums = 0
for i in range(n):
    sums += A[i]
    mod[i] = sums%m

mod_cnt = [0 for _ in range(m)]
for a in mod:
    mod_cnt[a] += 1

ans = mod_cnt[0]
for i in range(m):
    ans += mod_cnt[i] * (mod_cnt[i]-1) //2
print(ans)
