from collections import deque

class Deque:
    
    def __init__(self):
        self.cards = deque()

    def abandon(self):
        self.cards.popleft()

    def move(self):
        num = self.cards[0]
        self.cards.popleft()
        self.cards.append(num)

N = int(input())

card = Deque()

for i in range(1,N+1):
    card.cards.append(i)


while len(card.cards) > 1:
    card.abandon()
    card.move()

print(card.cards[0])
