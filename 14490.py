from math import gcd
n,m = map(int, input().split(":"))
gcd = gcd(n,m)
print(str(n//gcd)+":"+str(m//gcd))