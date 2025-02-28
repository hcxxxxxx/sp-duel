"""
Splendor Board Game: Displayed Cards Module

This file contains classes and methods related to managing and displaying cards in the Splendor board game.
It uses the Kivy framework for the graphical user interface.

Classes:

*> Popup used when a card that can be used as any color is picked. <*
*> This popup lets the user choose which color will be that card. <*
- ColorButton: Represents a button with a specific color that triggers an action when pressed.
- AnyCardPopupCard: Displays options for selecting a color for a card with the "ANY" color type.
- AnyCardPopup: A popup window for selecting a color for a card with the "ANY" color type.

*> Popup used when a component of cards is clicked on. <*
*> This lets the user see more details of the cards and choose one. <*
- CardButton: Represents a button for displaying detailed information about a game card.
- DisplayedCardPopupCard: Displays cards in a horizontal layout within a popup.
- DisplayedCardPopup: A popup window for displaying cards at a specific level.

*> This is the general class of displayed cards. <*
- DisplayedCards: Represents a group of displayed cards with associated actions.

"""

from functools import partial

from kivy.clock import Clock
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from models import GemType


class ColorButton(Button):
    """
    Represents a button with a specific color that triggers an action when pressed.

    Attributes:
    - text: The text displayed on the button (color).
    - card_color: The color associated with the button.
    - caller_displayed_cards: Reference to the parent DisplayedCards instance.
    - card: The card associated with the button.

    Methods:
    - on_press(): Triggered when the button is pressed. Calls draw_card_any method on the parent DisplayedCards instance.
    """
    def __init__(self, color=None, caller_displayed_cards=None, card=None, **kwargs):
        super(ColorButton, self).__init__(**kwargs)
        self.text = str(color)
        self.card_color = color
        self.caller_displayed_cards = caller_displayed_cards
        self.card = card

    def on_press(self):
        self.caller_displayed_cards.draw_card_any(self.card, self.card_color)


class AnyCardPopupCard(BoxLayout):
    """
    Displays options for selecting a color for a card with the "ANY" color type.

    Attributes:
    - caller_displayed_cards: Reference to the parent DisplayedCards instance.
    - card: The card associated with the popup.

    Methods:
    - build_ui(): Constructs the UI with ColorButton instances for each available color.
    - get_non_null(): Retrieves a list of non-null colors based on the player's owned cards.
    """
    def __init__(self, caller_displayed_cards=None, card=None, **kwargs):
        super(AnyCardPopupCard, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.caller_displayed_cards = caller_displayed_cards
        self.card = card
        self.build_ui()

    def build_ui(self):
        color_list = self.get_non_null()
        for color in color_list:
            card_button = ColorButton(color=color, caller_displayed_cards=self.caller_displayed_cards, card=self.card)
            self.add_widget(card_button)

    def get_non_null(self):
        owned_cards = self.caller_displayed_cards.parent.parent.current_player.owned_cards
        owned_colors = []
        for color in GemType:
            if color != GemType.GOLD and color != GemType.ANY:
                color_cards = owned_cards.get_card_widget(color)
                if len(color_cards.cards) > 0:
                    owned_colors.append(color)
        return owned_colors


class AnyCardPopup(Popup):
    """
    A popup window for selecting a color for a card with the "ANY" color type.

    Attributes:
    - caller_displayed_cards: Reference to the parent DisplayedCards instance.
    - card: The card associated with the popup.
    """
    def __init__(self, caller_displayed_cards=None, card=None, **kwargs):
        super(AnyCardPopup, self).__init__(**kwargs)
        self.title = f'Which color should be this card?'
        self.size_hint = (.3, .3)
        self.auto_dismiss = True
        self.caller_displayed_cards = caller_displayed_cards
        popup_card = AnyCardPopupCard(caller_displayed_cards=self.caller_displayed_cards, card=card)
        self.add_widget(popup_card)


class CardButton(Button):
    """
    Represents a button for displaying detailed information about a game card.

    Attributes:
    - card: The card associated with the button.
    - disabled: Flag indicating whether the button is disabled.
    - caller_displayed_cards: Reference to the parent DisplayedCards instance.

    Methods:
    - on_press(): Triggered when the button is pressed. Calls draw_card method on the parent DisplayedCards instance.
    - get_card_text(): Generates text containing detailed information about the associated card.
    - display_cost(): Generates text representation of the card's cost.
    """
    def __init__(self, card=None, disabled=True, caller_displayed_cards=None, **kwargs):
        super(CardButton, self).__init__(**kwargs)
        self.card = card
        self.disabled = disabled
        card_text = self.get_card_text()
        self.text = card_text
        self.caller_displayed_cards = caller_displayed_cards

    def on_press(self):
        self.caller_displayed_cards.draw_card(self.card)

    def get_card_text(self):
        return (
            f'ID: {self.card.card_id}\n'
            f'Color: {self.card.value} {self.card.color}\n'
            f'Victory points: {self.card.victory_points}\n'
            f'Crowns: {self.card.crowns}\n'
            f'Special effect: {self.card.special_effect}\n\n'
            f'Cost:\n{self.display_cost()}\n'
        )

    def display_cost(self):
        return '\n'.join([f'- {color}: {value}' for color, value in self.card.cost.items()])


class DisplayedCardPopupCard(BoxLayout):
    """
    Displays cards in a horizontal layout within a popup.

    Attributes:
    - cards: List of cards to be displayed.
    - caller_displayed_cards: Reference to the parent DisplayedCards instance.

    Methods:
    - build_ui(): Constructs the UI with CardButton instances for each card.
    - compute_has_enough_tokens(): Checks if the player has enough tokens to buy a specific card.
    - is_there_any_color_card_in_hand(): Checks if there are cards of any color in the player's hand.
    """
    def __init__(self, cards=None, caller_displayed_cards=None, **kwargs):
        super(DisplayedCardPopupCard, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.cards = cards
        self.caller_displayed_cards = caller_displayed_cards
        self.build_ui()

    def build_ui(self):
        for card in self.cards:
            enough_tokens = self.compute_has_enough_tokens(card=card)
            card_button = CardButton(card=card, disabled=not enough_tokens,
                                     caller_displayed_cards=self.caller_displayed_cards)
            self.add_widget(card_button)

    def compute_has_enough_tokens(self, card):
        owned_tokens = self.caller_displayed_cards.parent.parent.current_player.owned_tokens.tokens
        owned_cards = self.caller_displayed_cards.parent.parent.current_player.owned_cards
        color_card_in_hand = self.is_there_any_color_card_in_hand()
        jokers = owned_tokens[GemType.GOLD]
        for color, required_tokens in card.cost.items():
            num_card_color = owned_cards.get_card_widget(color).num_tokens
            available_tokens = owned_tokens[color]
            delta_token = max(0, required_tokens - available_tokens - num_card_color)
            jokers -= delta_token
            if jokers < 0:
                return False
            if card.color == GemType.ANY and not color_card_in_hand:
                return False
        return True

    def is_there_any_color_card_in_hand(self):
        owned_cards = self.caller_displayed_cards.parent.parent.current_player.owned_cards
        for color_cards in owned_cards.card_widgets.values():
            if len(color_cards.cards) > 0:
                return True
        return False


class DisplayedCardPopup(Popup):
    """
    A popup window for displaying cards at a specific level.

    Attributes:
    - level: The level of the cards to be displayed.
    - caller_displayed_cards: Reference to the parent DisplayedCards instance.
    """
    def __init__(self, level=None, cards=None, caller_displayed_cards=None, **kwargs):
        super(DisplayedCardPopup, self).__init__(**kwargs)
        self.title = f'Cards level {level}'
        self.size_hint = (.8, .8)
        self.auto_dismiss = True
        popup_card = DisplayedCardPopupCard(cards=cards, caller_displayed_cards=caller_displayed_cards)
        self.add_widget(popup_card)


class DisplayedCards(ButtonBehavior, BoxLayout):
    """
    Represents a group of displayed cards with associated actions.

    Attributes:
    - max_cards: Maximum number of cards to be displayed.
    - cards: List of cards currently displayed.
    - level: The level of the cards.
    - deck: Reference to the deck of cards.
    - popup: Reference to the displayed card popup.
    - popup_color: Reference to the any card popup for selecting color.

    Methods:
    - on_press(): Triggered when the button is pressed. Opens the DisplayedCardPopup.
    - show_cards(): Clears and updates the UI with labels for each card.
    - fill_cards(): Fills empty slots in the cards list with new cards from the deck.
    - remove_card(): Removes a specific card from the cards list.
    - draw_card(): Initiates the process of drawing a card from the display.
    - draw_card_any(): Initiates the process of drawing a card with "ANY" color type.
    - open_any_card_popup(): Opens the AnyCardPopup for selecting color.
    """
    cards = None

    def __init__(self, max_cards=None, level=None, deck=None, **kwargs):
        super(DisplayedCards, self).__init__(**kwargs)
        self.popup_color = None
        self.orientation = 'vertical'
        self.max_cards = max_cards
        self.cards = [None] * self.max_cards
        self.level = level
        self.deck = deck
        self.popup = None
        self.fill_cards()
        self.show_cards()

    def on_press(self):
        if not self.parent.parent.choosing_token_on_board:
            self.popup = DisplayedCardPopup(level=self.level, cards=self.cards, caller_displayed_cards=self)
            self.popup.open()

    def show_cards(self):
        self.clear_widgets()
        for card in self.cards:
            label_text = f'Card level {card.level} (id: {card.card_id})'
            label = Label(text=label_text)
            self.add_widget(label)

    def fill_cards(self):
        for card_position in range(len(self.cards)):
            if self.cards[card_position] is None:
                self.cards[card_position] = self.deck.draw_card()

    def remove_card(self, card):
        self.cards = [None if x == card else x for x in self.cards]

    def draw_card(self, card):
        if card.color == GemType.ANY:
            # Delay the opening of the AnyCardPopup by scheduling it after a short delay
            Clock.schedule_once(partial(self.open_any_card_popup, card), 0.1)
        else:
            # Continue with the rest of the draw_card logic for other card types
            self.remove_card(card)
            self.fill_cards()
            self.show_cards()
            self.popup.dismiss()

            current_player = self.parent.parent.current_player
            current_player.owned_cards.get_card_widget(card.color).add_card(card)

    def draw_card_any(self, card, color):
        self.remove_card(card)
        self.fill_cards()
        self.show_cards()
        self.popup_color.dismiss()
        self.popup.dismiss()
        current_player = self.parent.parent.current_player
        card.color = color
        current_player.owned_cards.get_card_widget(card.color).add_card(card)

    def open_any_card_popup(self, card, dt):
        self.popup_color = AnyCardPopup(card=card, caller_displayed_cards=self)
        self.popup_color.open()

    def __str__(self):
        return f'{self.cards}'
