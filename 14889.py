from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
players = set(range(N))
steams = combinations(players, N//2)
ans = 999999999
for steam in steams:
    steam = set(steam) ; lteam = players - steam
    s_stat = 0 ; l_stat = 0
    s_comb = combinations(steam,2) ; l_comb = combinations(lteam,2)
    for x in s_comb:
        s_stat += S[x[0]][x[1]]
        s_stat += S[x[1]][x[0]]
    for y in l_comb:
        l_stat += S[y[0]][y[1]]
        l_stat += S[y[1]][y[0]]
    ans = min(ans, abs(s_stat-l_stat))

print(ans)