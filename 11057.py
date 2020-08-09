N = int(input())
dp = [1]*10
for _ in range(N-1):
    for i in range(1,10):
        dp[i] += dp[i-1]
print(sum(dp)%10007)