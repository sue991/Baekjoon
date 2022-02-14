import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
set_A= list(sorted(set(A)))

dic = {}
for i, x in enumerate(set_A):
    dic[x] = i

for x in A:
    print(dic[x], end=" ")