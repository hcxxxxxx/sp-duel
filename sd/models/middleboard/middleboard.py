from kivy.uix.boxlayout import BoxLayout

from models import CROWN_CARDS, LEVEL1_CARDS, LEVEL2_CARDS, LEVEL3_CARDS
from models.middleboard.board import Board
from models.middleboard.crown_cards import CrownCards
from models.unit.decks import Deck
from models.middleboard.displayed_cards import DisplayedCards
from models.middleboard.scrolls import Scrolls


class MiddleBoard(BoxLayout):

    def __init__(self, tokenbag=None, **kwargs):
        super(MiddleBoard, self).__init__(**kwargs)
        self.cards_size = (.25, 1)
        crown_cards = CrownCards(deck=Deck(db_cards=CROWN_CARDS), size_hint=self.cards_size)
        self.add_widget(crown_cards)
        self.scrolls = Scrolls(size_hint=(.25, 1))
        self.add_widget(self.scrolls)
        self.board = Board(tokenbag=tokenbag)
        self.add_widget(self.board)
        self.displayed_cards1 = DisplayedCards(max_cards=5, level=1, deck=Deck(db_cards=LEVEL1_CARDS), size_hint=self.cards_size)
        self.add_widget(self.displayed_cards1)
        self.displayed_cards2 = DisplayedCards(max_cards=4, level=2, deck=Deck(db_cards=LEVEL2_CARDS), size_hint=self.cards_size)
        self.add_widget(self.displayed_cards2)
        self.displayed_cards3 = DisplayedCards(max_cards=3, level=3, deck=Deck(db_cards=LEVEL3_CARDS), size_hint=self.cards_size)
        self.add_widget(self.displayed_cards3)
