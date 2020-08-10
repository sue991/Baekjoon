T = int(input())
for _ in range(T):
    n = input()
    ans = ""
    for i in range(len(n)):
        if i%2 == 0:
            tmp = int(n[i])*2
            if tmp > 9: tmp = tmp%10 + tmp//10
            ans += str(tmp)
        else:
            ans += n[i]
    m = 0
    for x in ans:
        m += int(x)
    if m%10:
        print("F")
    else:
        print("T")