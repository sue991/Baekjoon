N = int(input())
a,b = 0,0
for _ in range(N):
    A,B = map(int, input().split())
    if A > B:
        a += 1
    elif A < B:
        b += 1

print(a,b)