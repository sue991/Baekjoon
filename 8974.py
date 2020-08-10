A,B = map(int, input().split())
A-=1
num = [[i]*i for i in range(1,50)]
num = sum(num,[])
print(sum(num[A:B]))