from collections import deque
T = int(input())
for _ in range(T):
    pwd = deque()
    tmp = deque()
    inputs = input()
    for x in inputs:
        if not pwd:
            if tmp:
                if x == ">":
                    pwd.append(tmp.popleft())
                elif x == "<" or x == "-":
                    continue
                else:
                    pwd.append(x)
            else:
                if x != ">" and x != "<" and x != "-":
                    pwd.append(x)
        else:
            if tmp:
                if x == ">":
                    pwd.append(tmp.popleft())
                    continue 
            if x == "<":
                tmp.appendleft(pwd.pop())
            elif x == "-":
                pwd.pop()
            elif x == ">":
                continue
            else:
                pwd.append(x)
    for x in pwd:
        print(x,end="")
    for x in tmp:
        print(x,end="")
    print()

        