p1 = list(map(int, input().split()))
p2 = list(map(int, input().split()))

P1 = 0; P2 = 0
win = False
for i in range(9):
    P1 += p1[i]
    if P1 > P2: win = True
    P2 += p2[i]
    if P1 > P2: win = True
if win:
    print("Yes")
else:
    print("No")