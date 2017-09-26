import Card
import Deck
import Shoe
import Hand

def get_value(self):
    value = sum(card.point for card in self.cards)
    aces = sum(card.is_ace for card in self.cards)
    while (value > 21) and aces:
        value -= 10
        aces -= 1
    return value