import numpy as np
import random

# Deals 5 cards from a deck to four players.
# Originally, the code printed stuff like "{'rank': 'Diamonds', 'suit': '4'}"
# so the rank and suit labels have been switched around.
random.seed(52)
ranks = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]

# Shuffles cards.
random.shuffle(deck)

# Deals cards to players.
deal = {f'{i+1}': [] for i in range(4)}
for _ in range(5):
    for player in deal:
        a = deck.pop()
        deal[player].append(a)

# Prints the cards in each player's hand.
for player, hand in deal.items():
    results = ', '.join([f"{card['rank']} of {card['suit']}" for card in hand])
    print(f"{player}'s hand: {results}")
