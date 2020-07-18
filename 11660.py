import copy, sys

N, M = map(int, sys.stdin.readline().split())

mat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
sum_mat = copy.deepcopy(mat)

for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            pass
        elif i == 0:
            sum_mat[i][j] += sum_mat[i][j-1]
        elif j == 0:
            sum_mat[i][j] += sum_mat[i-1][j]
        else:
            sum_mat[i][j] += sum(mat[i][:j]) + sum_mat[i-1][j]

for _ in range(M):
    x1,y1, x2,y2 = map(int, sys.stdin.readline().split())
    x1 -= 1 ; y1 -= 1 ; x2 -= 1 ; y2 -= 1
    if x1 == 0 and y1 == 0:
        print(sum_mat[x2][y2])
    elif x1 == 0:
        print(sum_mat[x2][y2] - sum_mat[x2][y1-1])
    elif y1 == 0:
         print(sum_mat[x2][y2] - sum_mat[x1-1][y2])
    else:
        print(sum_mat[x2][y2] - sum_mat[x2][y1-1] - sum_mat[x1-1][y2] + sum_mat[x1-1][y1-1])