from kivy.config import Config
Config.set('graphics', 'width', '1920')
Config.set('graphics', 'height', '720')

from kivy.app import App

from models.game import Game


class SplendorApp(App):
    def build(self):
        return Game()


if __name__ == '__main__':
    SplendorApp().run()
