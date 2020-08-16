n, s, m = map(int, input().split())
lst = list(map(int, input().split()))

dp1 = [0 for i in range(m + 1)]
dp2 = [0 for i in range(m + 1)]

dp1[s] = 1
for v in lst:
    for i in range(m + 1):
        if dp1[i]:
            if i + v <= m:
                dp2[i + v] = 1
            if i - v >= 0:
                dp2[i - v] = 1
    dp1 = dp2
    dp2 = [0] * (m + 1)

ans = -1
for i in range(m, -1, -1):
    if dp1[i]:
        ans = i
        break
print(ans)