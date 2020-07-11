N, M = map(int, input().split())
tree = list(map(int, input().split()))

def binary():
    start = 1 ; end = 1000000000
    while start <= end:
        mid = (start+end)//2
        n = 0
        for h in tree:
            if h > mid :
                n += h - mid
        if n >= M:
            start = mid + 1
        else:
            end = mid - 1
    return end
    
print(binary())