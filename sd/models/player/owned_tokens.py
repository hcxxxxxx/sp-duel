from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from models.unit.token import GemType


class OwnedTokens(BoxLayout):
    def __init__(self, **kwargs):
        super(OwnedTokens, self).__init__(**kwargs)
        self.tokens = {GemType.RED: 0, GemType.GREEN: 0, GemType.BLUE: 0, GemType.BLACK: 0, GemType.WHITE: 0,
                       GemType.PEARL: 0, GemType.GOLD: 0}
        self.token_widgets = {}
        self.update_widgets()

    def add_tokens(self, tokens_list):
        for token in tokens_list:
            self.tokens[token.gem_type] += 1
        self.clear_widgets()
        self.update_widgets()

    def remove_tokens(self, tokens_dict_to_pay=None):
        for color in tokens_dict_to_pay:
            owned_color = self.parent.owned_cards.get_card_widget(color).num_tokens
            if self.tokens[color] < tokens_dict_to_pay[color] - owned_color:
                self.tokens[GemType.GOLD] -= tokens_dict_to_pay[color] - self.tokens[color]
                self.tokens[color] = 0
            else:
                self.tokens[color] -= tokens_dict_to_pay[color] - owned_color
        self.update_widgets()

    def update_widgets(self):
        self.clear_widgets()
        self.token_widgets = {}
        for color in GemType:
            if color != GemType.ANY:
                token_color = Label(text=str(self.tokens[color]) + ' ' + str(color))
                self.token_widgets[color] = token_color
                self.add_widget(token_color)

    def get_tokens_widget(self, color):
        return self.token_widgets.get(color)

    def take_token(self, color):
        self.tokens[color] -= 1
        self.update_widgets()

    def add_token(self, color):
        self.tokens[color] += 1
        self.update_widgets()
