t = int(input())
for _ in range(t):
    n = int(input())
    p1,p2 = 0,0
    for _ in range(n):
        P1,P2 = input().split()
        if (P1 == 'R' and P2 == 'S') or(P1 == "S" and P2 == 'P') or(P1 == "P" and P2 == 'R'):
            p1 += 1
        elif P1 == P2:
            continue
        else:
            p2 += 1
    if p1 > p2:
        print("Player 1")
    elif p1 < p2:
        print("Player 2")
    else:
        print("TIE")