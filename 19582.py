import sys
input = sys.stdin.readline

N = int(input())

contest = []
for _ in range(N):
    x,p = map(int, input().split())
    contest.append((x,p))

prize = 0
num = 0  #참가 "안하는" 대회 수
chk = 1
max_p = 0 
for i in range(N):
    if prize <= contest[i][0]: #참가
        prize += contest[i][1]
        max_p = max(max_p,contest[i][1])
    else:
        if num == 0: #N-1
            if i == N-1:
                break
            num += 1
            if max_p > contest[i][1]:
                prize -= max_p
                if prize <= contest[i][0]:
                    prize += contest[i][1]
                else:
                    prize += max_p
                    continue
            else:
                continue
        else:
            chk = 0
            break

print("Kkeo-eok" if chk else "Zzz")