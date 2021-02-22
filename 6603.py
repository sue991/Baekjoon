import sys
from itertools import combinations
input = sys.stdin.readline

while True:
    k = list(map(int, input().split()))
    if k == [0]:    break
    S = k[1:]   
    comb = combinations(S,6)
    for s in comb:
        print(*s)
    print()