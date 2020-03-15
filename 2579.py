n = int(input())
stair = [0,]
for _ in range(n):
    stair.append(int(input()))

sum_num = [0,]

if n == 1:
    print(stair[1])
    exit()
else:
    sum_num.append(stair[1])
    sum_num.append(stair[1]+stair[2])


for i in range(3,n+1):
    sum_num.append(max(stair[i] + stair[i-1]+ sum_num[i-3], stair[i]+sum_num[i-2]))

print(sum_num[-1])

