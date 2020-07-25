import sys

T = int(sys.stdin.readline())

for _ in range(T):
    a,b = map(int, sys.stdin.readline().split())
    ans = ""
    if a%2 == 0:
        N = 1
        if b < 2 and a < 21:
            if a*(10**b) < 21:
                while(N < a*(10**b)):
                    ans += "-"
                    if len(ans) < 9:
                        ans += str(len(ans)+1)
                    else:
                        ans += str(len(ans)+2)
                    N = len(ans)
            else:
                ans = "-2-4-6-8-11-14-17..."
        else:
            ans = "-2-4-6-8-11-14-17..."
    else:
        N = 1
        if b < 2 and a < 21:
            if a*(10**b) < 21:
                while(N <= a*(10**b)):
                    ans += str(N)
                    if N != a*(10**b):
                        ans += "-"
                        if N < 7:
                            N += 2
                        else:
                            N += 3
                    else:
                        break
            else:
                ans = "1-3-5-7-10-13-16-..."
        else:
            ans = "1-3-5-7-10-13-16-..."

    print(ans)