T = int(input())
for _ in range(T):
    M,k = input().split()
    if k == "C":
        Q = input().split()
        for x in Q:
            print(ord(x)-64,end=" ")
    else:
        Q = list(map(int, input().split()))
        for x in Q:
            print(chr(x+64),end= " ")
    print()