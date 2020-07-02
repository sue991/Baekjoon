from collections import deque

class Deque:
    def __init__(self):
        self.nums = deque()

    def D(self):
        self.nums.popleft()

    def BD(self):
        self.nums.pop()

T = int(input())

for _ in range(T):
    queue = Deque()

    command = input()
    n = int(input())
    
    arr = input()
    arr = arr.strip("[]").split(",")
    if n == 0 : arr = []
    else:
        for x in arr:
            queue.nums.append(x)

    rev = False
    front_D = 0
    back_D = 0

    for c in command:
        if c == "R":
            rev = not rev
        elif c == "D":
            if rev:
                back_D += 1
            elif not rev:
                front_D += 1

    if front_D + back_D > len(queue.nums):
        print("error")

    else:
        for _ in range(front_D):
            queue.D()
        for _ in range(back_D):
            queue.BD()


        if rev:
            print("[",end="")
            for x in range(len(queue.nums)):
                if (len(queue.nums) == 1):
                    print(queue.nums[0],end='')
                else:
                    print(queue.nums[-1]+",",end='')
                queue.nums.pop()
            print("]")
                

        else:
            print("["+",".join(queue.nums)+"]")
