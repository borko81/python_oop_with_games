import random

SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack',
              'Queen', 'King')

NCARDS = 8


def getCard(deck):
    this_card = deck.pop()
    return this_card


def shuffle(deck):
    deck_out = deck.copy()
    random.shuffle(deck_out)
    return deck_out


starting_deck = []

for suit in SUIT_TUPLE:
    for value, rank in enumerate(RANK_TUPLE):
        card = {'rank': rank, 'suit': suit, 'value': value + 1}
        starting_deck.append(card)

score = 50

shuffle_deck = shuffle(starting_deck)

for _ in range(NCARDS):
    if score <= 0:
        break
    current_card = getCard(shuffle_deck)
    print(f"Rank is {rank} suit is {suit} and value is {value}".format(**current_card))
    next_card = getCard(shuffle_deck)
    answer = input('What is next ')
    correct = False
    if answer == 'h':
        if next_card['value'] > current_card['value']:
            score += 20
            correct = True
        else:
            score -= 20
    if answer == 'l':
        if next_card['value'] < current_card['value']:
            score += 20
            correct = True
        else:
            score -= 20
    print(next_card)
    print(correct, 'Score is %d' % score)
    correct = False

print("Game finish, score is %d" % score)
