import random

SUITS=[ "Clubs", "Diamonds", "Hearts", "Spades"]

RANKS =["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

DECK = []
SECONDDECK = []
for suit in SUITS:
    for rank in RANKS:
        DECK.append(rank + ' of ' + suit)

random.shuffle(DECK)

for card in DECK:
    print(card )

print('random draw = ' + random.choice(DECK))

for i in range(0,5):
    print(i)