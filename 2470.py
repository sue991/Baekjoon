N = int(input())
arr = list(map(int, input().split()))
start = 0
end = len(arr)-1

arr.sort()
ans = 2000000000

while(start < end):
    n = arr[start] + arr[end]
    if abs(n) < abs(ans):
        ans = n
        a = arr[start] ; b = arr[end]
    if n > 0:
        end -= 1
    elif n < 0:
        start += 1
    else:
        break
print(a,b)