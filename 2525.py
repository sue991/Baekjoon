A,B = map(int, input().split())
C = int(input())

tmp = C+B
while tmp >= 60:
    A+=1
    tmp -= 60
    if A >= 24:
        A = 0
print(A,tmp)