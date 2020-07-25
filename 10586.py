import copy, sys

N,M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
sum_num = []
ans = 0

for i in range(N):
    if i == 0:
        sum_num.append(nums[i])
    else:
        sum_num.append(sum_num[i-1] + nums[i])

for i in range(N):
    for j in range(i,N):
        if i == 0 and sum_num[j]%M == 0:
            ans += 1
        else:
            if (sum_num[j]-sum_num[i-1])%M == 0:
                ans += 1

print(ans)