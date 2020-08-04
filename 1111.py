N = int(input())
n = list(map(int, input().split()))
if N == 1 :
    print("A")
elif N == 2:
    if n[0] == n[1]:
        print(n[0])
    else:
        print("A")
else:
    if n[1]-n[0] == 0:
        a = 0
        b = n[1]
    else:
        a = (n[2]-n[1]) // (n[1]-n[0])
        b = n[1]-n[0]*a

    error = 0
    for i in range(N-1):
        if n[i]*a+b != n[i+1]:
            error = 1
            print("B")
            quit()
    if not error:
        print(n[-1]*a+b)