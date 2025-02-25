from kivy.uix.gridlayout import GridLayout

from models.player.owned_cards import OwnedCards
from models.player.owned_scrolls import OwnedScrolls
from models.player.owned_tokens import OwnedTokens
from models.player.reserved import Reserved


class Player(GridLayout):
    name = ''
    owned_tokens = None

    def __init__(self, reserved_cards, name, **kwargs):
        super(Player, self).__init__(**kwargs)
        self.name = name
        self.cols = 2
        self.size_hint = (.75, .5)
        self.pos_hint = {'center_x': .5}
        size_top = (1, .33)
        self.owned_tokens = OwnedTokens(size_hint=size_top)
        self.add_widget(self.owned_tokens)
        self.owned_scrolls = OwnedScrolls(size_hint=size_top)
        self.add_widget(self.owned_scrolls)
        self.owned_cards = OwnedCards()
        self.add_widget(self.owned_cards)
        self.reserved_cards = Reserved(reserved_cards=reserved_cards)
        self.add_widget(self.reserved_cards)

    def __str__(self):
        return f'{self.name}'

    def get_total_color(self):
        total_tokens = self.owned_tokens.tokens
        cards_colors = self.owned_cards.get_cards_colors()
        print(total_tokens)
        print(cards_colors)
