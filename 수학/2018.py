"""
i개의 수의 합
sums: sum(1,...,i)
n에서 i개의 수의 합을 빼서 나온 값을 i개로 나눴을 때 나머지가 0이면, 
n은 i개의 연속된 수의 합으로 만들 수 있다는 의미
"""

n = int(input())

sums = 0
ans = 0
for i in range(1, n+1):
    sums += i
    if (n-sums) >= 0 and (n-sums)%i == 0:
        ans += 1
print(ans)
