N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]

min_num = None

for i in range(N-7):
    for j in range(M-7):
        num1, num2 = 0,0
        #W
        for k in range(8):
            for l in range(8):
                if k%2 == 0 and l%2 == 0 and board[i+k][j+l]=='B':
                    num1 += 1
                elif k%2 == 0 and l%2 != 0 and board[i+k][j+l]=='W':
                    num1 += 1
                elif k%2 != 0 and l%2 == 0 and board[i+k][j+l]=='W':
                    num1 += 1
                elif k%2 != 0 and l%2 != 0 and board[i+k][j+l]=='B':
                    num1 += 1
            #B
        for k in range(8):
            for l in range(8):
                if k%2 == 0 and l%2 == 0 and board[i+k][j+l]=='W':
                    num2 += 1
                elif k%2 == 0 and l%2 != 0 and board[i+k][j+l]=='B':
                    num2 += 1
                elif k%2 != 0 and l%2 == 0 and board[i+k][j+l]=='B':
                    num2 += 1
                elif k%2 != 0 and l%2 != 0 and board[i+k][j+l]=='W':
                    num2 += 1

        mini = num1 if num1 < num2 else num2
        if min_num is None:
            min_num = mini
        else:
            min_num = mini if min_num > mini else min_num

print(min_num)