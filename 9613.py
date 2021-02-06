from itertools import combinations
from math import gcd

t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))
    arr = arr[1:]
    comb = combinations(arr,2)
    ans = 0
    for num in comb:
        ans += gcd(num[0],num[1])
    print(ans)