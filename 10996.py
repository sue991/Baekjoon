n = int(input())

if n == 1:
    print("*")
    exit()
for i in range(n*2):
    for j in range(n):
        if (i%2 == 0 and j%2 == 0) or (i%2 != 0 and j%2 != 0):
            print("*",end="")
        else:
            print(" ", end="")
    print()