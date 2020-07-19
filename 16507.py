import sys, copy
R, C, Q = map(int, sys.stdin.readline().split())
photo = [list(map(int, sys.stdin.readline().split())) for i in range(R)]
sum_mat = copy.deepcopy(photo)

for i in range(R):
    for j in range(C):
        if i == 0 and j == 0:
            pass
        elif i == 0:
            sum_mat[i][j] += sum_mat[i][j-1]
        elif j == 0:
            sum_mat[i][j] += sum_mat[i-1][j]
        else:
            sum_mat[i][j] += sum(photo[i][:j]) + sum_mat[i-1][j]

for _ in range(Q):
    r1,c1,r2,c2 = map(int, sys.stdin.readline().split())
    r1 -= 1; c1 -= 1; r2 -= 1; c2 -= 1

    n = (r2-r1+1)*(c2-c1+1)
    if r1 == 0 and c1 == 0:
        print(sum_mat[r2][c2]//n)
    elif r1 == 0:
        print((sum_mat[r2][c2] - sum_mat[r2][c1-1])//n)
    elif c1 == 0:
         print((sum_mat[r2][c2] - sum_mat[r1-1][c2])//n)
    else:
        print((sum_mat[r2][c2] - sum_mat[r2][c1-1] - sum_mat[r1-1][c2] + sum_mat[r1-1][c1-1])//n)