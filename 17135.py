from itertools import combinations as comb
from copy import deepcopy
import sys

N, M, D = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

castle = [i for i in range(M)]
archer = comb(castle,3)
ans = 0

NOE = 0
for i in board:
    NOE += sum(i)

for x in archer:
    noe = NOE
    if noe == 0: break
    Map = deepcopy(board)
    kill = 0
    P = 0
    while P<N:
        if noe == 0: break
        target = [(-1,-1),(-1,-1),(-1,-1)]
        dis = [11,11,11]
        for i in range(N-1,N-D-1,-1):
            if i < 0: break
            for j in range(M):
                if i == N-1 and Map[i][j] == 1:
                    noe -= 1
                if Map[i][j] == 1: #적 있을때
                    for k in range(3):
                        d = abs(N-i) + abs(x[k]-j)
                        if d < dis[k] and d <= D:
                            dis[k] = d
                            target[k] = (i,j)
                        elif d == dis[k] and j < target[k][1] and d<=D:
                            target[k] = (i,j)

        for idx,(i,j) in enumerate(target): 

            if Map[i][j] == 1 and i >= 0 and j >= 0:
                Map[i][j] = 0
                kill += 1
                if i != N-1:
                    noe -=1
        Map = [[0]*M] + Map[:N-1]
        P+=1
    ans = max(ans,kill)
print(ans)