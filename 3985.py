from collections import Counter

L = int(input())
N = int(input())

maxi = -1
audience = []
ans = [-1,-1]
tmp = -1
roll = [0 for _ in range(L)]
for i in range(N):
    P,K = map(int, input().split())
    audience.append((P,K))
for i,(a,b) in enumerate(audience):
    if b-a > maxi:
        maxi = b-a
        ans[0] = i+1
    for j in range(a-1,b):
        if roll[j] == 0:
            roll[j] = i+1

cake = Counter(roll)
if cake.get(0):
    del cake[0]

for aud, get in cake.items():
    if tmp < get: 
        ans[1] = aud
        tmp = get
print(ans[0])
print(ans[1])


