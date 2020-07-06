from itertools import permutations

A,B = input().split()

B = int(B)

pmt = list(map(''.join, permutations(A)))

k = -1

for x in pmt:
    if x[0] != '0' and int(x)<=B:
        k = max(k,int(x))

print(k)