t = int(input())

def T(n):
    return n*(n+1)//2
def W(n):
    ans = 0
    for i in range(1,n+1):
        ans += i*T(i+1)
    return ans

for _ in range(t):
    n = int(input())
    print(W(n))