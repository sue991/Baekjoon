import sys

N = int(sys.stdin.readline())

facilities = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
maxi = -1
fac1 , fac2 = 0,0
for i in range(N-1):
    for j in range(i+1,N):
        a = facilities[i][0] - facilities[j][0]
        b = facilities[i][1] - facilities[j][1]
        if  a*a + b*b > maxi:
            maxi = a*a + b*b
            fac1 = i
            fac2 = j

