K,N = map(int, input().split())

lan = [int(input()) for _ in range(K)]

def binary():
    start = 1 ; end = max(lan)
    while start <= end:
        mid = (start+end)//2
        n = 0
        for i in lan:
            n += i // mid
        
        if n >= N:
            start = mid + 1
        else:
            end = mid - 1

    return end

print(binary())