K = int(input())
nums = []

while K>0:
    K-=1
    n = int(input())
    if n == 0:
        nums.pop()
    else:
        nums.append(n)
print(sum(nums))
