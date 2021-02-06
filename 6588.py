import sys

sieve = list(range(1000001))
sieve[1] = 0
for p in range(2, int(1000001**0.5)+1):
    if sieve[p] != 0:
        for q in range(2*p, 1000001, p):
            sieve[q] = 0


while True:
    n = int(sys.stdin.readline())
    if n == 0: break
    chk = 0
    for x in sieve:
        if x > n-x: 
            print("Goldbach's conjecture is wrong.")
            break
        if x and sieve[n-x]:
            print("{} = {} + {}".format(n,x,n-x))
            break