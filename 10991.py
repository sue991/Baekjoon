N = int(input())

for i in range(N):
    for j in range(N+i):
        if N-1-i <= j <= N-1+i:
            if N%2 == 0:
                if (i%2 == 0 and j%2 == 1) or (i%2 == 1 and j%2 == 0):
                    print("*",end="")
                else:
                    print(" ",end="")
            else:
                if (i%2 == 0 and j%2 == 0) or (i%2 == 1 and j%2 == 1):
                    print("*",end="")
                else:
                    print(" ",end="")
        else:
            print(" ",end="")
    print()