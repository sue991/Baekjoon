from itertools import combinations

arr = []
for _ in range(9):
    arr.append(int(input()))

comb = combinations(arr, 7)
for x in comb:
    if sum(x) == 100:
        x = list(x)
        x.sort()
        for a in x: print(a)
        break