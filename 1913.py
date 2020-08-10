N = int(input())
find = int(input())
dis = [-1,1,2,-2]
add = [-2,2,2,-2]
snail = [[0 for _ in range(N)] for _ in range(N)]
x,y = N//2,N//2
n=1
snail[x][y] = n
while n <= N**2:
    for i in range(4):
        if i == 0:
            for j in range(1,abs(dis[i])+1):
                n += 1
                if n>N**2:
                    break
                if n == find:
                    x1,y1 = x-j,y
                snail[x-j][y] = n
            x += dis[i]
        elif i == 3:
            for j in range(1,abs(dis[i])+1):
                n += 1
                if n == find:
                    x1,y1 = x,y-j
                if n>N**2:
                    break
                snail[x][y-j] = n
            y += dis[i]
        elif i == 1:
            for j in range(1,dis[i]+1):
                if j >= N:
                    break
                n += 1
                if n>N**2:
                    break
                if n == find:
                    x1,y1 = x,y+j
                snail[x][y+j] = n
            y += dis[i]
        else:
            for j in range(1,dis[i]+1):
                n += 1
                if n>N**2:
                    break
                if n == find:
                    x1,y1 = x+j,y
                snail[x+j][y] = n
            x += dis[i]
    for i in range(4):
        dis[i] += add[i]

for i in snail:
    for j in i:
        print(j,end=" ")
    print()
print(x1+1,y1+1)