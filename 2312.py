T = int(input())
for _ in range(T):
    N = int(input())
    i=2
    n = N
    ans = [0 for _ in range(n+1)]
    while n!=1:
        if n%i == 0:
            n = n/i
            ans[i] += 1
        else: i+=1
    for j in range(1,N+1):
        if ans[j] != 0:
            print(j,ans[j])