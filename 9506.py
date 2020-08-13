while True:
    n = int(input())
    if n == -1:
        break
    divisor = []
    for i in range(1,n):
        if n%i == 0:
            divisor.append(i)
    if sum(divisor) == n:
        print(n,"=",end=" ")
        for i in range(len(divisor)):
            if i != len(divisor)-1:
                print(divisor[i],"+",end=" ")
            else:
                print(divisor[i])
    else:
        print(n,"is NOT perfect.")
