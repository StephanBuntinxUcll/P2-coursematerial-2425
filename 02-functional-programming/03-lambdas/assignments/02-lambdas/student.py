from util import *

card1 = Card(4,"schoppen")

card2 = Card(6, "claveren")
card3 = Card(8, "claveren")
card4 = Card(1, "harten")
card5 = Card(4,"schoppen")

cards=[card1,card2, card3, card4, card5]

def group_by_suit(cards):
    fun = lambda cards : cards.suit
    return group_by(cards, fun)


# print(group_by_suit(cards))