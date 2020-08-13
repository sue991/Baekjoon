from collections import deque
N = int(input())
password = deque(input() for _ in range(N))
tmp = []
while password:
    pwd = password.popleft()
    tmp.append(pwd)
    for x in tmp:
        if len(x) != len(pwd):
            continue
        elif pwd[::-1] == x:
            print(len(pwd),pwd[len(pwd)//2])
