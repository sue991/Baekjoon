import sys
input = sys.stdin.readline

N = int(input())

road = list(map(int, input().split()))
oil = list(map(int, input().split()))
oil = oil[:-1]

mini = min(oil)
cur_oil = oil[0]
remain_road = sum(road)
cost = 0

for i, (r, o) in enumerate(zip(road, oil)):
    if o == mini:
        cost += o*remain_road
        break
    else:
        if o < cur_oil:
            cost += o*r
            remain_road -= r
            cur_oil = o
        else:
            cost += cur_oil*r
            remain_road -= r

print(cost)