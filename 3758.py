T = int(input())
for _ in range(T):
    n, k, t, m = map(int, input().split())
    
    score = [[0 for _ in range(k)] for _ in range(n)]
    rank = []
    seq = [0 for _ in range(n)]
    num = [0 for _ in range(n)]
    for i in range(m):
        entry = list(map(int, input().split()))
        seq[entry[0]-1] = i
        num[entry[0]-1] += 1
        if score[entry[0]-1][entry[1]-1] < entry[2]:
            score[entry[0]-1][entry[1]-1] = entry[2]
    for i in range(n):
        score[i].append(sum(score[i]))
        rank.append({"id" : i+1 , "score" : score[i][-1], "try" : num[i] , "seq" : seq[i]})

    rank = sorted(rank, key = lambda x: (-x["score"], x["try"],x["seq"]))
    ans = 0
    for i in rank:
        if i["id"] == t:
            print(ans+1)
            break
        else: 
            ans+=1