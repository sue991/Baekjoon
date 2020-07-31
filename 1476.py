E,S,M = map(int, input().split())
ans,e,s,m  = 1,1,1,1
while e!=E or s!=S or m!=M:
    ans += 1
    e = e%15 + 1
    s = s%28 + 1
    m = m%19 + 1
print(ans)