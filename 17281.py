from itertools import permutations
from collections import deque
import sys

N = int(input())

inning = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

play = permutations(range(1,9)) #타자 순서
ans = 0

for per in play:
    per = list(per)
    per.insert(3,0)
    idx = 0 # 타자 순서
    score = 0 # 전체 점수
    for i in range(N): #각 inning
        out = 0
        field = deque()
        sums = 0
        while idx < 9:
            hit = inning[i][per[idx]]
            if hit != 0:
                field.append(hit)
                sums += hit
                if sums >= 4:
                    while sums >= 4:
                        n = field.popleft()
                        sums -= n
                        score += 1
            else:
                out += 1

            idx = (idx+1) % 9
            if out >= 3:
                while field:
                    field.popleft()
                break

    ans = max(ans,score)

print(ans)