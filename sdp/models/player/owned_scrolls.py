from kivy.uix.label import Label


class OwnedScrolls(Label):
    scrolls = 0

    def __init__(self, **kwargs):
        super(OwnedScrolls, self).__init__(**kwargs)
        self.text = str(self.scrolls) + ' scrolls'

    def update_scrolls(self):
        self.text = str(self.scrolls) + ' scrolls'

    def take_scroll(self):
        self.scrolls += 1
        self.update_scrolls()

    def use_scroll(self):
        self.scrolls -= 1
        self.update_scrolls()
