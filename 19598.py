import sys
input = sys.stdin.readline
N = int(input())
conference = [list(map(int, input().split())) for _ in range(N)]
room = []
conference.sort()
for i in range(N):
    if i == 0:
        room.append(conference[i][1])
        continue
    chk = 1
    for j in range(len(room)):
        if conference[i][0] >= room[j]:
            chk = 0
            room[j] = conference[i][1]
            break
    if chk:
        room.append(conference[i][1])
print(len(room))