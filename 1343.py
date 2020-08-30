board = input()
error = 0
i = 0
while True:
    if i >= len(board): break
    if board[i:i+4] == "XXXX":
        board = board.replace("X","A",4)
        i += 4
    elif board[i:i+2] == "XX":
        board = board.replace("X","B",2)
        i += 2
    elif board[i] == ".":
        i += 1
    else:
        error = 1 ; break
print(-1 if error else board)