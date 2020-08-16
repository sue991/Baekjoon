from collections import deque
import sys

input = sys.stdin.readline

sen = list(input().rstrip("\n"))
cursor = len(sen)
r_cur = []

M = int(input())

for _ in range(M):
    order = input().strip()
    if order == "L" :
        if cursor > 0:
            cursor -= 1
            r_cur.append(sen.pop())

    elif order == "D":
        if r_cur:
            cursor += 1
            sen.append(r_cur.pop())
    
    elif order == "B":
        if cursor != 0:
            sen.pop()
            cursor -= 1
    else:
        sen.append(order[-1])
        cursor += 1

for x in sen:
        print(x,end="")

for x in r_cur[::-1]:
    print(x,end="")