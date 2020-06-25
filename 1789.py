S = int(input())

n, sum = 0,0
while(sum <= S):
    n += 1  
    sum += n
n -= 1
print(n)