N = int(input())
pmt = list(map(int, input().split()))

k = -1 #index 최대값

for i in range(len(pmt)-1):
    if pmt[i] < pmt[i+1]:
        k = i

if k == -1:
    print(-1)
else:
    min_i = 0
    for i in range(k+1,len(pmt)):
        if pmt[k]< pmt[i]:
            min_i = i   
    pmt[k] , pmt[min_i] = pmt[min_i], pmt[k]
    pmt2 = pmt[:k+1]+sorted(pmt[k+1:])
    
    for x in pmt2:
        print(x,end=" ")
    print()
