N = int(input())

paper = [list(map(int, input())) for _ in range(N)]

def div(n, paper):
    chk = 0 # 압축 가능한지 확인
    for i in range(n):
        chk += sum(paper[i])

    if chk == 0: # 전부 0
        print(0, end='')
    elif chk == n**2: # 전부 1
        print(1, end='')
    else: # 쪼개기
        print("(", end='')
        p1 = [paper[i][:n//2] for i in range(n//2)] # 왼 위
        p2 = [paper[i][n//2:] for i in range(n//2)] # 오 위
        p3 = [paper[i][:n//2] for i in range(n//2, n)] # 왼 아래
        p4 = [paper[i][n//2:] for i in range(n//2, n)] # 오 아래
        div(n//2, p1)
        div(n//2, p2)
        div(n//2, p3)
        div(n//2, p4)
        print(")", end='')

div(N, paper)