# Card and Deck Classes in Python

This project provides two Python classes, `Card` and `Deck`, for representing playing cards and a deck of cards, respectively. It allows you to create, shuffle, and deal cards from a standard 52-card deck, using the classic French suits.

This project was done for Colt Steele's Python bootcamp. I had a lot of fun making this and learning about class attributes, and instance methods.

## Classes

### Card

The `Card` class represents a single playing card.

**Attributes:**

*   `suits`: List of the four card suits: "spades", "hearts", "diamonds", "clubs".
*   `values`: List of the 13 card values: "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K".
*   `value`: The rank/value of the card (e.g., "A", "K", "7").
*   `suit`: The suit of the card (e.g., "spades", "hearts").

**Methods:**

*   `__init__(self, value, suit)`: Initializes a new `Card` object with the given value and suit.
*   `__repr__(self)`: Returns a string representation of the card (e.g., "K of hearts").

### Deck

The `Deck` class (obviously) represents a standard 52-card deck.

**Attributes:**

*   `cards`: A list of `Card` objects representing the cards in the deck.

**Methods:**

*   `__init__(self)`: Initializes a new `Deck` object with a standard 52-card deck in order.
*   `count(self)`: Returns the number of cards remaining in the deck.
*   `__repr__(self)`: Returns a string representation of the deck (e.g., "Deck of 52 cards").
*   `_deal(self, num)`: A private method that deals `num` cards from the top of the deck. Raises a `ValueError` if there are not enough cards to deal.
*   `shuffle(self)`: Shuffles the cards in the deck randomly. Raises a `ValueError` if the deck is not full (52 cards). Returns the deck object itself, rather than a new shuffled deck, to allow for method chaining.
*   `deal_card(self)`: Deals a single card from the top of the deck.
*   `deal_hand(self, num)`: Deals a hand of `num` cards from the top of the deck.

## Usage

Here's how you can use the `Card` and `Deck` classes for your playing card-related projects (after cloning the repo...):

```python
from deck import Deck, Card

# Create a new deck
my_deck = Deck()

# Shuffle the deck
my_deck.shuffle()

# Deal a card
card = my_deck.deal_card()
print(card)  # Output: e.g., 7 of diamonds

# Deal a hand of 5 cards
hand = my_deck.deal_hand(5)
print(hand)  # Output: e.g., [A of spades, 10 of hearts, ...]

# Check the number of cards left
print(my_deck.count()) # Output: 46

# Example of error handling
try:
    my_deck.deal_hand(50)
except ValueError as e:
    print(e) # Output: Not enough cards to deal 50 cards. Only 46 cards left.
