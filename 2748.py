n = int(input())

fib_arr = [0,1]

def fib(f1,f2,num):
    fn = f1+f2

    if num == 0:
        return fn

    else:
        return fib(f2,fn,num-1)

if n <= 1:
    print(fib_arr[n])
else:
    print(fib(0,1,n-2))
    