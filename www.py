import sys

T = int(sys.stdin.readline())

for _ in range(T):
    a,b = map(int, sys.stdin.readline().split())
    ans = ""
    if b == 0 and a < 10:
        N = 1
        if a%2 == 0:

            while(N != a):
                ans += "-"
                ans += str(len(ans)+1)
                N = len(ans)
        else:
            while(N <= a):
                ans += str(N)
                if N != a:
                    ans += "-"
                N += 2

    elif 
    print(ans)

    # if a%3 == 0:
        
    # elif a%3 == 1:

    # else:
