from itertools import permutations
import sys
input = sys.stdin.readline

def cal(x,opt,y):
    if opt == "+":
        return x+y
    elif opt == "-":
        return x-y
    elif opt == "*":
        return x*y
    else:
        if x < 0:
            return -(abs(x)//y)
        else:
            return x//y

N = int(input())
A = list(map(int, input().split()))
n = list(map(int, input().split())) #  +,-,*,/
O = '+'*n[0] + '-'*n[1] + '*'*n[2] + '/'*n[3]
operator = permutations(O)

mini = 10000000000
maxi = -10000000000
for opt in operator:
    tmp = A[0] #중간 계산과정
    for i in range(1,N):
        tmp = cal(tmp,opt[i-1],A[i])
    mini = min(tmp, mini)
    maxi = max(tmp,maxi)
print(maxi) ; print(mini)