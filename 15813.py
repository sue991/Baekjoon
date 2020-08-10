N = int(input())
name = input()
ans = 0
for x in name:
    ans += ord(x)-64
print(ans)