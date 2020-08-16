N = int(input())
ans = 0
for _ in range(N):
    arr = list(input())
    chk = []
    for x in arr:
        if not chk:
            chk.append(x)
            continue
        else:
            if x == chk[-1]:
                chk.pop()
            else:
                chk.append(x)
    if not chk:
        ans += 1
print(ans)