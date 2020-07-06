from itertools import permutations

N = int(input())

pmt = [x for x in range(1,N+1)]

permut = list(permutations(pmt,N))

for x in permut:
    for y in x:
        print(y,end = " ")
    print()