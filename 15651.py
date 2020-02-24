N,M = map(int, input().split())

num_list = [i+1 for i in range(N)]

arr = []

def dfs(k):
    if k == M:
        print(*arr)
        return

    for i in range(N):
        arr.append(num_list[i])
        dfs(k+1)
        arr.pop()

dfs(0)