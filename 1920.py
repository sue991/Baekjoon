N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
chk = map(int, input().split())

def binary_search(arr, x):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (start+end) // 2
        if x == arr[mid]:
            return 1
        elif x > arr[mid]:
            start = mid+1
        else:
            end = mid-1
    return 0
    
for i in chk:
    print(binary_search(A,i))