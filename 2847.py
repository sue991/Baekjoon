N = int(input())
score = list(int(input()) for _ in range(N))
ans = 0
for i in range(N-2,-1,-1):
    while score[i] >= score[i+1]:
        ans += 1
        score[i] -= 1
print(ans)