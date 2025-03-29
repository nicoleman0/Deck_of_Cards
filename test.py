import unittest
from deck import Card, Deck


class CardTests(unittest.TestCase):
    def setUp(self):
        self.card = Card("A", "hearts")

    def test_init(self):
        self.assertEqual(self.card.value, "A")
        self.assertEqual(self.card.suit, "hearts")

    def test_repr(self):
        self.assertEqual(repr(self.card), "A of hearts")


class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        self.assertEqual(self.deck.count(), 52)

    def test_repr(self):
        self.assertEqual(repr(self.deck), "Deck of 52 cards")

    def test_iter(self):
        for card in self.deck:
            self.assertIsInstance(card, Card)

    def test_count(self):
        self.assertEqual(self.deck.count(), 52)

    def test_deal_card(self):
        card = self.deck.deal_card()
        self.assertIsInstance(card, Card)

    def test_deal_hand(self):
        hand = self.deck.deal_hand(5)
        self.assertEqual(len(hand), 5)

    def test_shuffle(self):
        self.deck.shuffle()
        self.assertEqual(self.deck.count(), 52)


if __name__ == "__main__":
    unittest.main()
