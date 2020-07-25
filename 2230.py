import sys

N,M = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(N)]
nums.sort()

start = 0
end = 0

ans = 2000000000

while(start != len(nums) and end != len(nums)):
    n = nums[end] - nums[start]
    if n == M:
        ans = n
        break
    
    elif n < M:
        end += 1
  
    if n >= M:
        start += 1
        if n < ans:
            ans = n

print(ans)
        

