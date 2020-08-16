from collections import deque
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    doc = list(map(int, input().split()))
    if N == 1:
        print(1)
        continue
    lst = deque()
    for i in range(N):
        lst.append([doc[i],i])
    
    ans = 0
    while lst:
        maxi = max(lst)[0]
        importance, idx = lst.popleft()
        if importance == maxi:
            ans += 1
            if idx == M:    break
        else:
            lst.append([importance, idx])
    print(ans)