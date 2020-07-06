from itertools import permutations

N = int(input())

num = map(int, input().split())

permut = list(permutations(num,N))

sums = []

for x in permut:
    k = 0
    for i in range(len(x)-1):
        k += abs(x[i]-x[i+1])
    sums.append(k)
print(max(sums))