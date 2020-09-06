import sys
input = sys.stdin.readline

T = int(input())
s = [[], [1], [6, 2, 4, 8], [1, 3, 9, 7], [6, 4], [5], [6], [1, 7, 9, 3], [6, 8, 4, 2], [1, 9]]
for _ in range(T):
    a,b = map(int, input().split())
    a %= 10
    if a == 0:
        print(10)
    else:
        print(s[a][b % len(s[a])])