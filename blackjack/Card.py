class Card:
    # First create fixed variabls for suit and rank
    SUITS = ["Diamonds", "Hearts", "Clubs", "Spades"]
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def card_name(self):
        card_name = "{} {}".format(self.rank, self.suit)  # Designates card_name as representation of objects
        return card_name

    def is_ace(self):
        return self.rank == 'A'

    def __str__(self):
        return "{} {}".format(self.rank, self.suit)

    def __repr__(self):
        return "{} {}".format(self.rank, self.suit)


# class NumValue(Card):
#     # Contains values for all cards whose value is the numeric equivalent of their rank (2-10)
#     def __init__(self):
#         Card.__init__(self, suit, rank)
#         self.card_value = assign_value()
#
#     def assign_value(self):
#         card_value = int(self.rank)
#         return card_value
#
#
# class HardValue(Card):
#     # Contains values for all face cards, whose value is always 10
#     def __init__(self, suit, rank):
#         Card.__init__(self, suit, rank)
#         self.card_value = assign_value()
#
#     def assign_value(self):
#         card_value = 0
#         if self.rank == "Jack", "Queen", or "King":
#             card_value += 10
#         elif self.rank == "Ace"
#             card_value += 1
#         return card_value
#
#
# class SoftValue(Card):
#     # Contains values for all Aces, the value of which will have to be determined under certain conditions
#     def __init__(self, suit, rank):
#         Card.__init__(self, suit, rank)
#         self.card_value = assign_value()
#
#     def assign_value(self):
#         card_value = 0
#         if self.rank == "Two", "Three", "Four", "Five", "Six", "Seven",
#                         "Eight", "Nine", "Ten":
#             card_value
#
#         if self.rank == "Jack", "Queen", or "King":
#             card_value += 10
#         elif self.rank == "Ace"
#             card_value += 11
#         return card_value

