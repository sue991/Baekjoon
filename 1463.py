n = int(input())

cal = [0,0,1,1,]

def dp(k):
    sum_num = [0,0,0]
    if k%3 == 0:
        sum_num[0] = 1+cal[int(k/3)]
    if k%2 == 0:
        sum_num[1] = 1+cal[int(k/2)]
    sum_num[2] = cal[k-1]+1
    mini = []
    for x in sum_num:
        if x >0:
            mini.append(x)
    return min(mini)



for i in range(4,n+1):
    cal.append(dp(i))

print(cal[n])
