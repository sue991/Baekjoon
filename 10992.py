N = int(input())
for i in range(N):
    for j in range(N+i):
        if i != N-1 and (j == N-1-i or j == N-1+i):
            print("*",end="")
        elif i == N-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()