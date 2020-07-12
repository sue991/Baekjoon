N = int(input())

std = sorted([list(map(int, input().split())) for _ in range(N)], key= lambda x: -x[2])

print(*std[0][:2])
print(*std[1][:2])

if std[0][0] == std[1][0]:
    print(*std[3][:2])
else:
    print(*std[2][:2])