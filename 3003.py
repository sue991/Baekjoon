chess= [1,1,2,2,2,8]
p = list(map(int, input().split()))
for i in range(6):
    print(chess[i]-p[i],end =" ")
