A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

a,b = 0,0
a = A*P
if C < P:
    b = B + (P-C)*D
else:
    b = B

if a < b:
    print(a)
else:
    print(b)