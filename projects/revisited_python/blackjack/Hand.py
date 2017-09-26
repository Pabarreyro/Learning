import Card

class Hand:
    def __init__(self):
        Card.__init__(
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)
        return self.hand

    def assign_points(self, card):
        if rank == 'A':
            self.point = 11
        elif rank in ['K', 'Q', 'J']:
            self.point = 10
        else:
            self.point = int(rank)