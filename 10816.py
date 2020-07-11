N = int(input())
sang = list(map(int, input().split()))
M = int(input())
card = list(map(int, input().split()))

dic = {}

for x in sang:
    try:
        dic[x] += 1
    except:
        dic[x] = 1
ans = []
for n in card:
    try:
        ans.append(dic[n])
    except:
        ans.append(0)

for i in ans:
    print(i,end=" ")