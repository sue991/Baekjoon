import sys
from math import gcd
input = sys.stdin.readline

N = int(input())
r = list(map(int, input().split()))

for x in r[1:]:
    if gcd(r[0], x) == 1:
        print(f"{r[0]}/{x}")
    else:
        print(f"{r[0]//gcd(r[0], x)}/{x//gcd(r[0], x)}")