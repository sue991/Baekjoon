N,M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
M,K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]
ans = [[0 for _ in range(K)] for _ in range(N)]

for i in range(N):
    for j in range(K):
        s = 0
        for k in range(M):
            ans[i][j] += A[i][k] * B[k][j]

for i in ans:
    for j in i:
        print(j,end = " ")
    print()