N = int(input())
num = sorted(list(set(map(int, input().split()))))
print(*num)
