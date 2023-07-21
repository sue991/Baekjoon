import sys
input = sys.stdin.readline
from collections import deque

def move_belt():
    global belt, robot
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0

def move_robot():
    global belt, robot
    for i in range(N-2, -1, -1):
        if robot[i] == 1 and robot[i+1] == 0 and belt[i+1]:
            robot[i+1] = 1
            robot[i] = 0
            belt[i+1] -= 1
    robot[-1] = 0

def put_robot():
    global belt, robot
    if not robot[0] and belt[0]:
        robot[0] = 1
        belt[0] -= 1

def count_zero():
    global belt
    cnt = 0
    for b in belt:
        if not b:
            cnt += 1
    return cnt


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    belt = deque(A)
    robot = deque([0] * N)

    stage = 0
    while True:
        stage+=1
        move_belt()
        move_robot()
        put_robot()
        cnt = count_zero()
        if cnt >= K:
            break
    print(stage)