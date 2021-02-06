from math import gcd

def lcm(x,y):
    return x*y//gcd(x,y)


T = int(input())
for _ in range(T):
    a,b = map(int, input().split())
    print(lcm(a,b))



