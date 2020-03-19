n = int(input())

num = [[0 for _ in range(10)] for _ in range(101)]

for i in range(1,10):
    num[1][i] = 1

for i in range(2,n+1):
    for j in range(10):
        if j == 0:
            num[i][j] = num[i-1][1]
        elif j == 9:
            num[i][j] = num[i-1][8]
        else:
            num[i][j] = num[i-1][j-1] + num[i-1][j+1]

print(sum(num[n])%1000000000)