from Chapter_1.Card import Card


class Deck:
    ranks = [str(i) for i in range(2, 11)] + list("JQKA")
    suits = "pik karo trefl kier".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __getitem__(self, position):
        return self._cards[position]

    def __len__(self):
        return len(self._cards)

    def __repr__(self) -> str:
        return f"{super().__repr__()} - with cards: {self._cards}"

    def __str__(self) -> str:
        return f"cards: {self._cards}"
