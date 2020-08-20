import sys
input = sys.stdin.readline

score = 0

def test():
    for i in range(10):
        for j in range(10):
            if(i>=4 and j>=4): continue
            print(board[i][j], end=" ")
        print("")

def mov_blue(t,x,y,s): # blue에 떨구기 지우는건 나중에~
    if t == 1 or t == 2:
        chk = 0
        for i in range(4,9):
            if board[x][i+1] != 0:
                chk = 1
                board[x][i] = s
                if t == 2:
                    board[x][i-1] = s
                break
        if not chk:
            board[x][9] = s
            if t == 2:
                board[x][8] = s
    else: # t == 3
        chk = 0
        for i in range(4,9):
            if board[x][i+1] or board[x+1][i+1]:
                chk = 1
                board[x][i] = s ; board[x+1][i] = s
                break
        if not chk:
            board[x][9] = s ; board[x+1][9] = s

def mov_green(t,x,y,s):
    if t == 1 or t == 3:
        chk = 0
        for i in range(4,9):
            if board[i+1][y] != 0:
                chk = 1
                board[i][y] = s
                if t == 3:
                    board[i-1][y] = s
                break
        if not chk:
            board[9][y] = s
            if t == 3:
                board[8][y] = s

    else: # t == 2
        chk = 0
        for i in range(4,9):
            if board[i+1][y] or board[i+1][y+1]:
                chk = 1
                board[i][y] = s ; board[i][y+1] = s
                break
        if not chk:
            board[9][y] = s ; board[9][y+1] = s

def get_blue(): # get score
    global flag
    global score
    while True:
        check = 1
        for i in range(9,5,-1):
            chk = 1
            for j in range(4):
                if board[j][i] == 0:
                    chk = 0
                    break
            if chk: # 세로가 전부 > 0
                score += 1
                check = 0
                flag = 0
                for j in range(4):
                    if block_num_b[board[j][i]] == 2:
                        block_num_b[board[j][i]] = 1
                    board[j] = board[j][:4] + [0] + board[j][4:i] + board[j][i+1:]
                # moving(2)
        if check:
            break

def get_green(): # get score
    global score
    global board
    global flag
    while True:
        check = 1
        for i in range(9,5,-1):
            chk = 1
            for j in range(4):
                if board[i][j] == 0:
                    chk = 0
                    break
            if chk: #가로가 전부 > 0
                score += 1
                check = 0
                flag = 0
                for j in range(4):
                    if block_num_g[board[i][j]] == 3:
                            block_num_g[board[i][j]] = 1
                board = board[:4] + [[0]*10] + board[4:i] + board[i+1:]
                # moving(1)
        if check:
            break

def moving(t):
    global flag
    if t == 1: #green
        while True:
            check = 1
            for i in range(4):
                while True:
                    chk = 1
                    for j in range(9,4,-1): # 한 줄 확인
                        if board[j][i] == 0 and board[j-1][i] != 0:
                            if block_num_g[board[j-1][i]] != 2:   #내려야됨
                                board[j][i] , board[j-1][i] = board[j-1][i] , board[j][i]
                                chk = 0
                                check = 0
                                flag = 0
                            else: #2일때
                                if i < 4 and board[j][i+1] == 0 and block_num_g[board[j-1][i+1]] == 2:
                                    board[j][i] , board[j-1][i] = board[j-1][i] , board[j][i]
                                    board[j][i+1] , board[j-1][i+1] = board[j-1][i+1] , board[j][i+1]
                                    chk = 0
                                    check = 0
                                    flag = 0

                    if chk:
                        break
            if check:
                break

    elif t == 2: #blue
        while True:
            check = 1
            for i in range(4):
                while True:
                    chk = 1
                    for j in range(9,4,-1):
                        if board[i][j] == 0 and board[i][j-1] != 0:
                            if block_num_b[board[i][j-1]] != 3: #내리자
                                board[i][j] , board[i][j-1] = board[i][j-1] , board[i][j]
                                chk = 0
                                check = 0
                            else: #3인데 내려야돼
                                if i < 4 and board[i+1][j] == 0 and block_num_b[board[i+1][j-1]] == 3:
                                    board[i][j] , board[i][j-1] = board[i][j-1] , board[i][j]
                                    board[i+1][j] , board[i+1][j-1] = board[i+1][j-1] , board[i+1][j]
                                    chk = 0
                                    check = 0
                    if chk:
                        break
            
            if check:
                break




def del_blue(): # 삐져나온거 지우기
    chk = 0
    for i in range(4):
        if board[i][5] > 0:
            chk = 1
            break
    if chk:
        for j in range(4):
            board[j] = board[j][:4] + [0] + board[j][4:9]
        return True
    else:
        return False

def del_green():
    global board
    chk = 0
    for i in range(4):
        if board[5][i] > 0:
            chk = 1
            break
    if chk:
        board = board[:4] + [[0]*10] + board[4:9]
        return True
    else: 
        return False

def count():
    cnt = 0
    for i in range(4):
        for j in range(6,10):
            if board[i][j] > 0:
                cnt += 1
            if board[j][i] > 0:
                cnt += 1
    return cnt


if __name__ == "__main__":
    board = [[0 for _ in range(10)] for _ in range(10)]
    check = [[0 for _ in range(10)] for _ in range(10)]

    N = int(input())
    s = 1
    block_num_b = [0,]
    block_num_g = [0,]
    for _ in range(N):
        t,x,y = map(int, input().split())
        block_num_b.append(t)
        block_num_g.append(t)
        mov_blue(t,x,y,s)
        mov_green(t,x,y,s)
        while True:
            flag = 1
            get_blue()
            get_green()
            moving(1)
            moving(2)
            if flag:
                break

        while del_blue() or del_green():
            continue
        
        s += 1
    print(score)
    print(count())