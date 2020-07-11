def binary(x):
    start = 0 ; end = N-1
    while start <= end:
        mid = (start+end)//2
        if x == sang[mid]:
            return 1
        elif x > sang[mid]:
            start = mid+1
        else:
            end = mid-1
    return 0

N = int(input())
sang = list(map(int, input().split()))
M = int(input())
card = list(map(int, input().split()))

sang.sort()
for x in card:
    print(binary(x),end=" ")