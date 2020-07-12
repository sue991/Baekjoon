N = int(input())
budget = list(map(int, input().split()))
M = int(input())


def binary():
    start = 0 ; end = max(budget)
    while start <= end or n > M:
        mid = (start+end)//2
        n = 0
        for x in budget:
            if x >= mid:
                n += mid
            else:
                n += x
        if n > M:
            end = mid - 1
        else:
            start = mid + 1
    return mid
    
print(binary())