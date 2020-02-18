N = int(input())

lst = []

for _ in range(N):
    lst.append(list(input().split()))

lst.sort(key= lambda x: int(x[0]))

for i in lst:
    print(i[0],i[1])
