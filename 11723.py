import sys
input = sys.stdin.readline
s = set()

M = int(input())
for _ in range(M):
    order = input().split()
    if order[0] == "all":
        s = set(range(1,21))
        continue
    elif order[0] == "empty":
        s.clear()
        continue
    x = int(order[1])
    if order[0] == "add":
        s.add(x)
    elif order[0] == "remove":
        s.discard(x)
    elif order[0] == "check":
        print(1 if x in s else 0)
    elif order[0] == "toggle":
        if x in s:  s.remove(x)
        else:   s.add(x)
