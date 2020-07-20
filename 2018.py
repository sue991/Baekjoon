N = int(input())

start = 1
end = 1
ans = 0
sums = 1
while(start < N):

    if sums >= N or end == N:
        sums -= start
        start += 1
    else:
        end += 1
        sums += end
    if sums == N:
        ans += 1

print(ans)