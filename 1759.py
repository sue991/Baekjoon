import sys
input = sys.stdin.readline

vowels = ['a','e','i','o','u']
# consonants
L, C = map(int, input().split())
t = input().split()
t.sort()
print(t)