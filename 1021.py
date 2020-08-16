from collections import deque

class Deque:
    def __init__(self,T):
        self.lst = deque(x+1 for x in range(T))
        self.cnt = 0

    def D(self):
        self.lst.popleft()

    def move_left(self):
        self.cnt += 1
        tmp = self.lst.popleft()
        self.lst.append(tmp)

    def move_right(self):
        self.cnt += 1
        tmp = self.lst.pop()
        self.lst.appendleft(tmp)


    def length(self):
        return len(self.lst)

N, M = map(int, input().split())
q = Deque(N)
nums = deque(map(int, input().split()))

while nums:
    n = nums.popleft()
    idx = q.lst.index(n)

    if q.lst[0] == n:
        q.D()
        continue
    
    else:
        if q.length()-1 - idx >= idx:
            for _ in range(idx):
                q.move_left()
        else:
            for _ in range(q.length() - idx):
                q.move_right()
        
    if q.lst[0] == n:
        q.D()

print(q.cnt)