import sys
input = sys.stdin.readline

def TSP(now, visited):
    if dp[now][visited]:
        return dp[now][visited]
    
    if visited == (1<<N) -1:
        return W[now][0] if W[now][0] > 0 else sys.maxsize

    cost = sys.maxsize

    for i in range(1,N):
        if not (visited >> i)%2 and W[now][i]: # 방문한 적이 없고, 길이 있을 때
            tmp = TSP(i, visited|(1<<i))
            cost = min(cost, tmp + W[now][i])

    dp[now][visited] = cost
    return cost    
    

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(1<<N) for _ in range(N)]

print(TSP(0,1))