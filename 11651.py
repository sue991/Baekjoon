N = int(input())

lst = [list(map(int, input().split()))  for _ in range(N)]

lst.sort(key=lambda x: (x[1],x[0]))

for i in lst:
    print(i[0],i[1])