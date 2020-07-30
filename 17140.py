from collections import Counter
import sys

r, c, k = map(int, sys.stdin.readline().split())
r -= 1 ; c -= 1
A = [list(map(int, input().split())) for _ in range(3)]

time = 0
while time <= 100:
    if r < len(A) and c < len(A[0]) and A[r][c] == k:
        print(time)
        break
    row = len(A)
    col = len(A[0])
    tmp = []
    max_len = 0
    if row >= col: #R
        for arr in A:
            cnt = Counter(arr)
            if cnt.get(0):
                del cnt[0]
            cnt = list(map(list, cnt.items()))
            cnt = sorted(cnt, key= lambda x: (x[1],x[0]))
            lst = list(sum(cnt, []))[:100]
            tmp.append(lst)
            if len(lst) > max_len:
                max_len = len(lst)
        
        for x in tmp:
            while len(x) < max_len:
                x.append(0)
        A = tmp
    else:   #C
        A = list(zip(*A))
        for arr in A:
            cnt = Counter(arr)
            if cnt.get(0):
                del cnt[0]
            cnt = list(map(list, cnt.items()))
            cnt = sorted(cnt, key= lambda x: (x[1],x[0]))
            lst = list(sum(cnt, []))[:100]
            tmp.append(lst)
            if len(lst) > max_len:
                max_len = len(lst)
        
        for x in tmp:
            while len(x) < max_len:
                x.append(0)
        A = tmp       
        A = list(zip(*A))
    time += 1
    
if time > 100:
    print(-1)