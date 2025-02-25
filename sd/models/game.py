import random
from enum import Enum

from kivy.clock import Clock
from kivy.graphics import Color, Line
from kivy.uix.boxlayout import BoxLayout

from models.middleboard.middleboard import MiddleBoard
from models.player.player import Player
from models.unit.tokenbag import TokenBag


class GameState(Enum):
    START = 1
    PLAYING = 2
    END = 3


class TurnState(Enum):
    START = 1
    PLAYING = 2
    END = 3


class Game(BoxLayout):
    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)

        self.orientation = 'vertical'
        self.spacing = 20

        self.player2 = Player(reserved_cards=[], name='player2')
        self.add_widget(self.player2)

        self.tokenbag = TokenBag()
        self.middleboard = MiddleBoard(tokenbag=self.tokenbag)
        self.add_widget(self.middleboard)

        self.player1 = Player(reserved_cards=[], name='player1')
        self.add_widget(self.player1)

        self.current_player = random.choice([self.player1, self.player2])
        self.opponent = self.player1 if self.current_player == self.player2 else self.player2
        self.game_state = GameState.START
        self.turn_state = None
        self.turn = None
        self.rectangle_instruction = None  # Store the instruction id for the rectangle

        self.choosing_token_on_board = False

        self.start_game()

    def start_game(self):
        self.game_state = GameState.PLAYING
        self.start_turn()

    def start_turn(self, *args):
        Clock.schedule_once(self.draw_current_player, 0.1)

    def end_turn(self):
        self.turn_state = TurnState.END
        self.current_player = self.player1 if self.current_player == self.player2 else self.player2
        self.opponent = self.player1 if self.current_player == self.player2 else self.player2
        self.start_turn()

    def draw_current_player(self, dt):
        if self.rectangle_instruction is not None:
            self.canvas.remove(self.rectangle_instruction)

        with self.canvas:
            Color(0, 1, 0, 1)
            self.rectangle_instruction = Line(
                rectangle=(
                    self.current_player.pos[0],
                    self.current_player.pos[1],
                    self.current_player.size[0],
                    self.current_player.size[1],
                ),
                width=2,
            )

    def on_size(self, instance, value):
        # Handle size changes here, e.g., update the drawing
        Clock.schedule_once(self.draw_current_player, 0.1)
