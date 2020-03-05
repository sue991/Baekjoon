N = int(input())

cost = [list(map(int, input().split())) for i in range(N)]

for i in range(1,N):
    cost[i][0] += min(cost[i-1][1],cost[i-1][2])
    cost[i][1] += min(cost[i-1][0],cost[i-1][2])
    cost[i][2] += min(cost[i-1][0],cost[i-1][1])

min_cost = min(cost[N-1][0],cost[N-1][1],cost[N-1][2])

print(min_cost)