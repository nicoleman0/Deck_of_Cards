from random import shuffle


class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = [Card(value, suit)
                      for suit in Card.suits for value in Card.values]

    def count(self):
        return len(self.cards)

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def _deal(self, num):
        if self.count() == 0:
            raise ValueError("All cards have been dealt!")
        if self.count() < num:
            raise ValueError(
                f"Not enough cards to deal {num} cards. Only {self.count()} cards left.")
        cards = self.cards[-num:]
        self.cards = self.cards[:-num]
        return cards

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled.")
        shuffle(self.cards)
        return self     # this allows for method chaining

    def deal_card(self):
        return self._deal(1)

    def deal_hand(self, num):
        return self._deal(num)


print(Deck().shuffle())
print(Deck().deal_card())
