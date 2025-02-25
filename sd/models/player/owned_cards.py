from functools import partial

from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from models import GemType, SpecialEffect


def get_index(lst, element):
    return [index for index, value in enumerate(lst) if value == element]


class TotalPointsCrowns(BoxLayout):
    def __init__(self, **kwargs):
        super(TotalPointsCrowns, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.total_points = 0
        self.total_crowns = 0
        self.build_ui()

    def update_points_crowns(self):
        self.total_points = 0
        self.total_crowns = 0
        for color in GemType:
            if color != GemType.GOLD and color != GemType.ANY:
                color_card = self.parent.get_card_widget(color)
                self.total_points += color_card.victory_points
                self.total_crowns += color_card.crowns
        self.clear_widgets()
        self.build_ui()

    def build_ui(self):
        self.add_widget(Label(text=f'total points={self.total_points}'))
        self.add_widget(Label(text=f'crowns={self.total_crowns}'))


class OwnedCardBox(BoxLayout):
    def __init__(self, color=None, **kwargs):
        super(OwnedCardBox, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.color = color
        self.num_tokens = 0
        self.victory_points = 0
        self.crowns = 0
        self.cards = []

        self.popup_colors = None

        self.indexes_tokens_to_choose = []

        self.build_ui()


    def add_card(self, card):
        self.cards.append(card)
        self.parent.parent.parent.current_player.owned_tokens.remove_tokens(card.cost)
        self.apply_special_effect(card)

    def after_special_effect(self):
        self.update_cards()
        self.parent.parent.parent.end_turn()

    def update_cards(self):
        self.cards = self.cards
        self.num_tokens = sum([card.value for card in self.cards])
        self.victory_points = sum([card.victory_points for card in self.cards])
        self.crowns = sum([card.crowns for card in self.cards])
        self.clear_widgets()
        self.build_ui()
        self.parent.points_crowns.update_points_crowns()

    def apply_special_effect(self, card):
        if card.special_effect == SpecialEffect.PLAY_AGAIN:
            current_player = self.parent.parent.parent.current_player
            player1 = self.parent.parent.parent.player1
            player2 = self.parent.parent.parent.player2
            self.parent.parent.parent.current_player = player1 if current_player == player2 else player2
            self.after_special_effect()
        elif card.special_effect == SpecialEffect.TAKE_SAME_COLOR:
            available_colors = []
            for row_index in self.parent.parent.parent.middleboard.board.board_gems:
                for token_index in row_index:
                    if token_index.gem_type not in available_colors:
                        available_colors.append(token_index.gem_type)
            self.indexes_tokens_to_choose = []
            if card.color in available_colors:
                board_gem = self.parent.parent.parent.middleboard.board.board_gems
                for row_index in range(len(board_gem)):
                    for token_index in range(len(board_gem[row_index])):
                        if board_gem[row_index][token_index].gem_type == card.color:
                            self.indexes_tokens_to_choose.append([row_index, token_index])
                self.parent.parent.parent.choosing_token_on_board = True
                Clock.schedule_once(
                    lambda dt: self.parent.parent.parent.middleboard.board.update_board(self.indexes_tokens_to_choose),
                    0.1)
            pass
        elif card.special_effect == SpecialEffect.TAKE_SCROLL:
            if self.parent.parent.parent.middleboard.scrolls.scrolls > 0:
                self.parent.parent.parent.middleboard.scrolls.take_scroll()
                self.parent.parent.parent.current_player.owned_scrolls.take_scroll()
            elif self.parent.parent.parent.opponent.owned_scrolls.scrolls > 0:
                self.parent.parent.parent.opponent.owned_scrolls.use_scroll()
                self.parent.parent.parent.current_player.owned_scrolls.scrolls.take_scroll()
            self.after_special_effect()
        elif card.special_effect == SpecialEffect.TAKE_OPPONENT_TOKEN:
            opponent_tokens = self.parent.parent.parent.opponent.owned_tokens.tokens.items()
            opponent_non_null_tokens = [color for color, value in opponent_tokens if value > 0]
            self.popup_colors = ColorsOpponent(opponent_non_null_tokens=opponent_non_null_tokens, caller_owned_card_box=self)
            self.popup_colors.bind(on_dismiss=lambda _: self.dismiss_popup(card))
            self.popup_colors.open()
        else:
            self.after_special_effect()

    def dismiss_popup(self, card):
        Clock.schedule_once(lambda dt: self.popup_colors.dismiss(), 0.1)
        self.after_special_effect()

    def build_ui(self):
        self.add_widget(Label(text=f'{self.color}'))
        self.add_widget(Label(text=f'tokens: {self.num_tokens}'))
        self.add_widget(Label(text=f'points: {self.victory_points}'))


class OwnedCards(BoxLayout):
    def __init__(self, **kwargs):
        super(OwnedCards, self).__init__(**kwargs)
        self.card_widgets = {}
        for color in GemType:
            if color != GemType.GOLD and color != GemType.ANY:
                card = OwnedCardBox(orientation='vertical', color=color)
                self.card_widgets[color] = card
                self.add_widget(card)

        card = OwnedCardBox(orientation='vertical', color='neutral')
        self.card_widgets['neutral'] = card
        self.add_widget(card)

        self.points_crowns = TotalPointsCrowns()
        self.add_widget(self.points_crowns)

    def get_card_widget(self, color):
        return self.card_widgets.get(color)

    def get_cards_colors(self):
        cards_colors = {}
        for color in GemType:
            if color != GemType.GOLD and color != GemType.ANY:
                cards_colors[color] = self.get_card_widget(color).num_tokens
        return cards_colors


class ColorButton(Button):
    """
    A button representing a color choice for a card.
    """
    def __init__(self, color_to_take=None, caller_owned_card_box=None, **kwargs):
        super(ColorButton, self).__init__(**kwargs)
        self.text = str(color_to_take)
        self.color_to_take = color_to_take
        self.caller_owned_card_box = caller_owned_card_box

    def on_press(self):
        """
        Triggered when the button is pressed.
        """
        self.caller_owned_card_box.parent.parent.parent.current_player.owned_tokens.add_token(self.color_to_take)
        self.caller_owned_card_box.parent.parent.parent.opponent.owned_tokens.take_token(self.color_to_take)
        self.caller_owned_card_box.popup_colors.dismiss()


class AnyCardPopupCard(BoxLayout):
    """
    The layout for displaying color choices in the AnyCardPopup.
    """
    def __init__(self, opponent_non_null_tokens=None, caller_owned_card_box=None, **kwargs):
        super(AnyCardPopupCard, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.opponent_non_null_tokens = opponent_non_null_tokens
        self.caller_owned_card_box = caller_owned_card_box
        self.build_ui()

    def build_ui(self):
        """
        Build the UI with ColorButton widgets for each available color.
        """
        for color_to_take in self.opponent_non_null_tokens:
            card_button = ColorButton(color_to_take=color_to_take, caller_owned_card_box=self.caller_owned_card_box)
            self.add_widget(card_button)


class ColorsOpponent(Popup):
    """
    Popup for selecting a color when drawing a card with type ANY.
    """
    def __init__(self, opponent_non_null_tokens=None, caller_owned_card_box=None, **kwargs):
        super(ColorsOpponent, self).__init__(**kwargs)
        self.title = f'Which token would you like to steal?'
        self.size_hint = (.3, .3)
        self.auto_dismiss = False
        popup_card = AnyCardPopupCard(opponent_non_null_tokens=opponent_non_null_tokens,
                                      caller_owned_card_box=caller_owned_card_box)
        self.add_widget(popup_card)
