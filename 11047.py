import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = []
for i in range(N):
   A.append(int(input()))

num = 0
for i in range(-1, -N-1, -1):
    if A[i] > K:
        continue
    elif A[i] <= K:
        num += K // A[i]
        K = K % A[i]

    if K == 0:
        print(num)
        break