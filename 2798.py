N,M = map(int, input().split())

cards = list(map(int, input().split()))

sum_cards = 0

for i in range(len(cards)-2):
    for j in range(i+1,len(cards)-1):
        for k in range(j+1,len(cards)):
            sum_num = cards[i] + cards[j] + cards[k]
            if sum_num >= sum_cards and sum_num <= M:
                sum_cards = sum_num

print(sum_cards)