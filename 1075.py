N = int(input()[:-2] + "00")
F = int(input())
while N%F != 0:
    N += 1
print(str(N)[-2:])