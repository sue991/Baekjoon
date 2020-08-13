import sys
n,k = map(int, sys.stdin.readline().split())

cal = []
for i in range(1,n+1):
    if i == 1:
        cal.append(i)
    else:
        cal.append(cal[i-2]*i)
print((cal[n-1]//cal[k-1]//cal[n-k-1])%10007)