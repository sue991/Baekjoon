N = int(input())
star = "* "*N
for i in range(N):
    if i%2 == 0:
        print(star)
    else:
        print(" "+star)