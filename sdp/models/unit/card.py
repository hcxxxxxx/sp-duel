from enum import Enum


class SpecialEffect(Enum):
    PLAY_AGAIN = 1
    TAKE_SAME_COLOR = 2
    TAKE_SCROLL = 3
    TAKE_OPPONENT_TOKEN = 4

    def __str__(self):
        return f'{self.name}'


class Card:
    card_id = None
    level = None
    cost = None
    value = None
    color = None
    crowns = None
    victory_points = None
    special_effect = None

    def __init__(self, card_id=None, level=None, cost=None, value=None, color=None, crowns=None, victory_points=None,
                 special_effect=None):
        self.card_id = card_id
        self.level = level
        self.cost = cost
        self.value = value
        self.color = color
        self.crowns = crowns
        self.victory_points = victory_points
        self.special_effect = special_effect

    def __str__(self):
        return f'{self.card_id}'

    def __repr__(self):
        return f'{self.card_id}'
