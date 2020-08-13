from math import factorial as fac
n = int(input())
num = str(fac(n))[::-1]
ans = 0
for x in num:
    if x == '0':
        ans += 1
    else:
        break
print(ans)