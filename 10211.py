import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    X = list(map(int, sys.stdin.readline().split()))
    max_sum = []
    for i in range(N):
        if i == 0:
            max_sum.append(X[0])
        else:
            max_sum.append(X[i] + max_sum[i-1])
    
    maxi = max(max_sum)
    for i in range(1,len(max_sum)):
        for j in range(i):
            if max_sum[i] - max_sum[j] > maxi:
                maxi = max_sum[i] - max_sum[j]
    print(maxi)