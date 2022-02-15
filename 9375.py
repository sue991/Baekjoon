import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    d = {}
    for _ in range(n):  
        name, type = input().split()
        if type in d:
            d[type].append(name)
        else:
            d[type] = [name]
    
    cnt = 1
    for k, v in d.items():
        cnt *= (len(v)+1)
    print(cnt-1)