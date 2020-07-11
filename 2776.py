
def binary(x):
    start = 0 ; end = N-1
    while start <= end:
        mid = (start+end)//2
        if x == note1[mid]:
            return 1
        elif x > note1[mid]:
            start = mid+1
        else:
            end = mid-1
    return 0

T = int(input())
for _ in range(T):
    N = int(input())
    note1 = list(map(int, input().split()))
    M = int(input())
    note2 = list(map(int, input().split()))

    note1.sort()
    for x in note2:
        print(binary(x))
