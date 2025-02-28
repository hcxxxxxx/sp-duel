from kivy.core.window import Window
from kivy.graphics import Ellipse
from kivy.metrics import dp
from kivy.uix.widget import Widget


class Scrolls(Widget):
    def __init__(self,  **kwargs):
        super(Scrolls, self).__init__(**kwargs)
        self.scrolls = 3
        self.orientation = 'vertical'
        self.circle_size = dp(20)
        self.circle_instructions = []
        self.circle_instruction = None
        self.update_scrolls()

    def on_size(self, *args):
        self.update_scrolls()

    def update_scrolls(self):
        self.canvas.clear()
        for i in range(1, self.scrolls + 1):
            y_position = self.height * i / (self.scrolls + 1) - self.circle_size / 2
            position = (self.center_x - self.circle_size / 2, self.y + y_position)
            self.circle_instruction = Ellipse(size=(self.circle_size, self.circle_size), pos=position)
            self.circle_instructions.append(self.circle_instruction)
            self.canvas.add(self.circle_instruction)

    def take_scroll(self):
        self.scrolls -= 1
        self.update_scrolls()