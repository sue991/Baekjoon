import math

n,m = map(int, input().split())
num = math.gcd(n,m)
print(num)
print((n*m)//num)