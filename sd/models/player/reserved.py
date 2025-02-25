from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class Reserved(BoxLayout):

    reserved_cards = []

    def __init__(self, reserved_cards, **kwargs):
        super(Reserved, self).__init__(**kwargs)
        self.reserved_cards = reserved_cards
        self.show_reserved_cards()

    def show_reserved_cards(self):
        self.clear_widgets()
        if len(self.reserved_cards) == 0:
            label = Label(text='no reserved cards')
            self.add_widget(label)
        else:
            cards_layout = BoxLayout()
            for card in self.reserved_cards:
                card_label = Label(text=card.card_id)
                cards_layout.add_widget(card_label)
            self.add_widget(cards_layout)

    def buy_card(self, index):
        card_bought = self.reserved_cards.pop(index)
        self.show_reserved_cards()
        return card_bought

    def reserve_card(self, card):
        self.reserved_cards.append(card)
        self.show_reserved_cards()
