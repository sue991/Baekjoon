chess = [input() for _ in range(8)]
ans = 0
for i in range(8):
    for j in range(8):
        if i%2 and j%2 and chess[i][j] == "F":
            ans += 1
        elif not i%2 and not j%2 and chess[i][j] == "F":
            ans += 1
print(ans)