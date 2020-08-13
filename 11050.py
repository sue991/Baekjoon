N,K = map(int, input().split())
cal = 1
n = 1
for i in range(K):
    cal *= (N-i)
for i in range(1,K+1):
    n *= i
print(cal//n)