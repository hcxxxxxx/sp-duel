from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class CrownCards(BoxLayout):
    deck = None

    def __init__(self, deck=None, **kwargs):
        super(CrownCards, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.deck = deck
        self.show_cards()

    def show_cards(self):
        for card in self.deck.cards:
            str_label = f'{card.victory_points} victory points\n'
            if card.special_effect:
                special_effect = card.special_effect.name.lower()
                str_label += special_effect
            else:
                str_label += 'no effect'
            label = Label(text=str_label)
            self.add_widget(label)

    def draw_card(self, card_position):
        return self.cards.pop(card_position)

    def __str__(self):
        return f'{self.deck}'
