nums = list(map(int, input().split()))
n = int(input())

nums.sort()

ans = list()
i = 0
for x in nums:
    for y in nums[i+1:]:
        if x+y == n:
            ans.append([x,y])
    i += 1
cnt = len(ans)
for x in range(len(ans)):
    if x != 0 and ans[x][0] == ans[x-1][0] and ans[x][1] == ans[x-1][1]:
        cnt -= 1
        continue
    print('{0} {1}'.format(ans[x][0],ans[x][1]))

print(cnt)