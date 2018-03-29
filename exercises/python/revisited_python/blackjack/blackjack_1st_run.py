import random
# Must have...
# Card class: designate, view
# Deck class: shuffle, deal
# Hand class: hit, score
# Might need...
# Player class: Hand class object associated with it.
# Blackjack class: Main game logic.


class Card:  # Class containing empty attributes to be instantiated in another class
    def __init__(self, suit, rank, card_value=0):
        self.suit = suit
        self.rank = rank
        self.card_value = card_value

    def card_name(self):
        card_name = "{} {}".format(self.rank, self.suit)  # Designates card_name as representation of objects
        return card_name

    def __str__(self):
        return "{} {}".format(self.rank, self.suit)

    def __repr__(self):
        return "{} {}".format(self.rank, self.suit)


class Deck:
    def __init__(self):
        self.deck = self.deck_builder()  # Assigns output from function below to deck attribute

    def deck_builder(self):
        deck = []
        suit = ["Diamonds", "Hearts", "Clubs", "Spades"]
        card_value = {"Ace": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9,
                      "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}

        for i in suit:
            for x, y in card_value.items():
                deck.append(Card(i, x, y))  # Instantiates to the attributes designated in Card class
        random.shuffle(deck)
        return deck

    def __str__(self):
        return '{}'.format(self.deck)

    def __repr__(self):
        return '{}'.format(self.deck)


class Hand:
    def __init__(self):
        self.hand = []
        self.start_deck = Deck()
        self.deal = self.deal_hand()

    def deal_hand(self):
        player_hand = self.hand
        dealer_hand = self.hand
        deck = self.start_deck
        while len(dealer_hand) < 2:
            player_hand.append(deck[0])
            dealer_hand.append(deck[1])
        return player_hand, dealer_hand
        # print('{}\n{}\n{}\n'.format(player_hand, dealer_hand, deck))

    def __str__(self):
        return '{}'.format(self.hand)

    def __repr__(self):
        return '{}'.format(self.hand)


hand1 = Hand()
# print(hand1.start_deck)
print(hand1.deal)
# print(game1.deck)