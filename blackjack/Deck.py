import Card
import random


class Deck(Card):
    def __init__(self):
        self.deck = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        self.shuffle()

    def __str__(self):
        deck_of_cards = ''
        for card in self.deck:
            deck_of_cards += str(card), ' '
        return cards_in_deck

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        dealt_card = self.deck.pop(0)
        return dealt_card

game1 = Deck()
print(game1.deck)