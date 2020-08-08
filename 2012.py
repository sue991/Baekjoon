N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
ans = 0
n = 1
for x in arr:
    ans += abs(x-n)
    n += 1
print(ans)