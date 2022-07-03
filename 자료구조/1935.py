from collections import deque

dq = []

N = int(input())
eq = [x for x in input()]
digit = [int(input()) for _ in range(N)]

for x in eq:
    if x.isalpha():
        dq.append(digit[ord(x) - ord('A')])
    else:
        a = dq.pop()
        b = dq.pop()
        eval(f"dq.append({b} {x} {a})")
        
print("{:.2f}".format(dq[-1]))