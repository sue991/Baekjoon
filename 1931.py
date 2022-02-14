import sys

input = sys.stdin.readline
N = int(input())
A = []
for _ in range(N):
    A.append(tuple(map(int, input().split())))

A = sorted(A, key=lambda x: x[0])
A = sorted(A, key=lambda x: x[1])

cnt = 0
end = 0
for i in range(N):
    if A[i][0] == A[i][1] == end:
        cnt += 1
    
    elif A[i][0] >= end:
        cnt += 1
        end = A[i][1]


print(cnt)
