import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


cards = FrenchDeck()
for card in cards:
    print(card)

# highest spades->hearts->diamonds->clubs
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_highest_sorting(card_input: Card) -> int:
    rank_index = FrenchDeck.ranks.index(card_input.rank)
    return rank_index * len(suit_values) + suit_values[card_input.suit]


# for card in sorted(cards, key=spades_highest_sorting):
#     print(card)

