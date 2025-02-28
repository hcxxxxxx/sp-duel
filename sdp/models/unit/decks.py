import random


class Deck:

    def __init__(self, db_cards=None):
        self.cards = []
        self.cards.extend(db_cards)
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()



    def __str__(self):
        return f'{self.cards}'
