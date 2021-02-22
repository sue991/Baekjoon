import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
OPT = list(map(int, input().split()))

MIN = 1000000000
MAX = -1000000000
def opt(i, tmp, add, sub, mul, div):
    if i == N:
        global MIN, MAX
        MIN = min(tmp, MIN)
        MAX = max(tmp, MAX)
        return
    if add > 0 :    opt(i+1,tmp+A[i], add-1, sub, mul, div)
    if sub > 0 :    opt(i+1,tmp-A[i], add, sub-1, mul, div)
    if mul > 0 :    opt(i+1,tmp*A[i], add, sub, mul-1, div)
    if div > 0 :    
        if tmp > 0 :    opt(i+1,tmp//A[i], add, sub, mul, div-1)
        else :  opt(i+1,-(abs(tmp)//A[i]), add, sub, mul, div-1)

opt(1,A[0],OPT[0],OPT[1],OPT[2],OPT[3])
print(MAX)
print(MIN)