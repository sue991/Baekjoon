L,R,A = map(int, input().split())

ans = min(L,R)

L-=ans ; R-=ans
ans *= 2
if max(L,R) >= A:
    ans += A*2
else:
    ans += max(L,R)*2
    A-= max(L,R)
    ans += A//2 *2
print(ans)