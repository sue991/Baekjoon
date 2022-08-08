import sys
n = int(sys.stdin.readline())

change = [0 for _ in range(n+1)]

for i in range(1, n+1):
    if i < 5:
        if i%2 == 0:
            change[i] = i // 2
        else:
            change[i] = -1
        
    else:
        if change[i-5] != -1:
            change[i] = change[i-5] + 1
        else: # -1
            if i%2 == 0:
                change[i] = i // 2
            else:
                change[i] = -1

print(change[n])