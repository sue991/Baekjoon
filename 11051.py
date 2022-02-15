import sys
input = sys.stdin.readline

n, k = map(int, input().split())

k = min(k, n-k) ## nCk = nC(n-k)
dp = [[0] + [0 for _ in range(k)] for k in range(n+1)]

for i in range(1,n+1):
    for j in range(len(dp[i])):
        if j == 0 or j == i:
            dp[i][j] = 1
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % 10007
print(dp[n][k])