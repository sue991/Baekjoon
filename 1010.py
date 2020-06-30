from math import factorial as fac

T = int(input())

for i in range(T):
    n,m = map(int, input().split())
    
    comb = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == j :
                comb[i-1][j-1] = 1
            if i > j :
                 continue
            else:
                if i==1:
                    comb[i-1][j-1] = j
                else:
                    comb[i-1][j-1] = comb[i-1][j-2] + comb[i-2][j-2]

    print(comb[n-1][m-1])