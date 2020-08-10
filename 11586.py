N = int(input())
mirror = [input() for _ in range(N)]
K = int(input())

if K == 1:
    for i in mirror:
        for j in i:
            print(j,end="")
        print()
elif K == 2:
    for i in mirror:
        for j in i[::-1]:
            print(j,end="")
        print()
else:
    for i in mirror[::-1]:
        for j in i:
            print(j,end="")
        print()