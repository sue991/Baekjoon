N = int(input())
board = sorted([list(map(int, input().split())) for _ in range(N)], key= lambda x: -x[2])

win = {}
k = 3 ; i = 0
while k > 0:
    if board[i][0] not in win: # 처음
        win[board[i][0]] = 1
        print(*board[i][:2])
        k -= 1 ; i += 1
    elif win[board[i][0]] == 1: # 두번쨰
        win[board[i][0]] += 1
        print(*board[i][:2])
        k -= 1 ; i += 1
    else: 
        i += 1
        continue