N,M = map(int, input().split())
sen = []
compare = []
ans = []
for _ in range(N):
    sen.append(input())
for _ in range(N):
    compare.append(input())
for i in range(N):
    tmp = ""
    for x in sen[i]:
        tmp += x*2
    ans.append(tmp)
error = 0
for i in range(N):
    if ans[i] != compare[i]:
        print("Not Eyfa")
        error = 1
        break
if not error:
    print("Eyfa")