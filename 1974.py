N, r, c = map(int, input().split())
ans = 0
while N > 0:
    tmp = 2**(N-1)
    if N > 1:
        if r < tmp <= c: # 제 2사분면
            ans += tmp**2
            c -= tmp

        elif c < tmp <= r: # 제 3사분면
            ans += (tmp**2) * 2
            r -= tmp
    
        elif tmp <= r and tmp <= c:# 제 4사분면
            ans += (tmp**2) * 3
            r -= tmp ; c -= tmp

    else: # N == 1
        if r == 0 and c == 1: #제 2사분면
            ans += 1
        elif r == 1 and c == 0: #제 3사분면
            ans += 2
        elif r == 1 and c == 1: #제 4사분면
            ans += 3
    N -= 1
print(ans)