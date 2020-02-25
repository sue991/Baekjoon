T = int(input())

for i in range(T):
    N = int(input())

    arr = [0,1,1,1,2,2,3,4,5,7,9,]

    if N > 10:
        for i in range(11,N+1):
            arr.append(arr[i-5]+ arr[i-1])

    print(arr[N])

