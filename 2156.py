n = int(input())

wine = [int(input()) for _ in range(n)]

dp = [0]
dp.append(wine[0])

if(n>1):
    dp.append(wine[0]+wine[1])


for i in range(3,n+1):
    case1 = wine[i-1] + dp[i-2]
    case2 = wine[i-1] + wine[i-2] + dp[i-3]
    case3 = dp[i-1]
    max_v = max(case1,case2,case3)

    dp.append(max_v)

print(dp[n])