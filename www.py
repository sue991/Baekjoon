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

    elif b < 2 and a < 21:
        if a*(10**b) < 21:
            if a%3 == 0:
                N = 9
                ans = "1-3-5-7-9"
                while(N != a*(10**b)):
                    ans += "-"
                    ans += str(N+3)
                    N += 3
            elif a%3 == 1:
                ans = "1-3-5-7-10"
                N = 10
                while(N != a*(10**b)):
                    ans += "-"
                    ans += str(N+3)
                    N += 3
            elif a%3 == 2:
                ans = "-2-4-6-8"
                N = 8
                while(N != a*(10**b)):
                    ans += "-"
                    ans += str(N+3)
                    N += 3
        else:
            if a%3 == 0:
                ans = "1-3-5-7-9-12-15-1..."
            elif a%3 == 1:
                ans = "1-3-5-7-10-13-16-..."
            else:
                ans = "-2-4-6-8-11-14-17..."

    else:
        if a%3 == 0:
            ans = "1-3-5-7-9-12-15-1..."
        elif a%3 == 1:
            ans = "1-3-5-7-10-13-16-..."
        else:
            ans = "-2-4-6-8-11-14-17..."
    print(ans)