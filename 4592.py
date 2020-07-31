while True:
    n = input()
    if n == '0':
        break
    else:
        n = list(map(int, n.split()))
        N = n[0]
        n = n[1:]
        q = []
        for i in range(N):
            if i==0:
                q.append(n[i])
            else:
                if q[-1] != n[i]:
                    q.append(n[i])
        q.append("$")
        print(*q)