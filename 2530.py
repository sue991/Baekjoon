A,B,C = map(int, input().split())
D = int(input())
tmp = D+C
while tmp >= 60:
    tmp -= 60
    B += 1
    if B >= 60:
        B -= 60
        A += 1
    if A >=24:
        A = 0
print(A,B,tmp)