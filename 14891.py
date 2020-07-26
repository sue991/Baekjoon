from collections import deque
import copy

gear = [deque(input()) for _ in range(4)]
K = int(input())

for _ in range(K):
    a,b = map(int, input().split())
    a -= 1

    chk = [0]*4
    chk[a] = b
    for i in reversed(range(a)): # 왼쪽 확인
        if (b == 1 and a%2 == 1) or (b == -1 and a%2 == 0):
            if gear[i][2] != gear[i+1][6]:
                if i%2 == 0:
                    chk[i] = -1
                else:
                    chk[i] = 1
            else:
                break
        else:
            if gear[i][2] != gear[i+1][6]:
                if i%2 == 0:
                    chk[i] = 1
                else:
                    chk[i] = -1
            else:
                break

    for i in range(a+1,4): #오른쪽 확인
        if (b == 1 and a%2 == 1) or (b == -1 and a%2 == 0):
            if gear[i][6] != gear[i-1][2]:
                if i%2 == 0:
                    chk[i] = -1
                else:
                    chk[i] = 1
            else:
                break
        else:
            if gear[i][6] != gear[i-1][2]:
                if i%2 == 0:
                    chk[i] = 1
                else:
                    chk[i] = -1
            else:
                break

    for i in range(4):
        if chk[i] == 1:
            gear[i].appendleft(gear[i].pop())
        elif chk[i] == -1:
            gear[i].append(gear[i].popleft())

ans = 0
if gear[0][0] == '1':
    ans += 1
if gear[1][0] == '1':
    ans += 2
if gear[2][0] == '1':
    ans += 4
if gear[3][0] == '1':
    ans += 8

print(ans)