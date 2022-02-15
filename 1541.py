import sys
input = sys.stdin.readline

A=input().split('-')

ans = 0
for i in range(len(A)):
    if i == 0:
        for x in A[i].split('+'):
            ans += int(x)
    else:
        for x in A[i].split('+'):
            ans -= int(x)

print(ans)