N, M = map(int, input().split())
arr = list(map(int, input().split()))

end = 0
start = 0
ans = 0
while(start < N):
    if sum(arr[start:end]) >= M or end == N:
        start += 1
    else:
        end += 1
    if sum(arr[start:end]) == M:
        ans += 1

print(ans)
