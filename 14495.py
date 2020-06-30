class F:
    def __init__(self):
        self.arr = [0,1,1,1]

    def add(self,n):
        self.arr.append(self.arr[n-1] + self.arr[n-3])

    def prn(self):
        print(self.arr[n])

f = F()
n = int(input())

if n < 4:
    pass
else:
    for i in range(4,n+1):
        f.add(i)

f.prn()