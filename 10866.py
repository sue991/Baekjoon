import sys
from collections import deque


class Deque:
    def __init__(self):
        self.dp = deque()

    def push_front(self, x):
        self.dp.appendleft(x)
    
    def push_back(self, x):
        self.dp.append(x)
    
    def pop_front(self):
        if self.dp:
            num = self.dp.popleft()
            return num
        else:
            return -1

    def pop_back(self):
        if self.dp:
            num = self.dp.pop()
            return num
        else:
            return -1

    def size(self):
        return len(self.dp)

    def empty(self):
        if self.dp:
            return 0
        else:
            return 1
    
    def front(self):
        if self.dp:
            return self.dp[0]
        else:
            return -1

    def back(self):
        if self.dp:
            return self.dp[-1]
        else:
            return -1

N = int(sys.stdin.readline())
case = Deque()

for _ in range(N):
    command = sys.stdin.readline().split()

    n = command[0]

    if n == 'push_front':
        case.push_front(command[1])
    elif n == "push_back":
        case.push_back(command[1])
    elif n == "pop_front":
        print(case.pop_front())
    elif n == "pop_back":
        print(case.pop_back())
    elif n == "size":
        print(case.size())
    elif n == "empty":
        print(case.empty())
    elif n == "front":
        print(case.front())
    elif n == "back":
        print(case.back())