from enum import Enum


class GemType(Enum):
    BLUE = 1
    WHITE = 2
    GREEN = 3
    BLACK = 4
    RED = 5
    PEARL = 6
    GOLD = 7
    ANY = 8

    def __str__(self):
        return f'{self.name.lower()}'


class Token:
    gem_type = None
    image = None

    def __init__(self, gem_type=None):
        self.gem_type = gem_type
        self.image = f'images/{self.gem_type.name}.jpeg'

    def __str__(self):
        return f'{self.gem_type}'

    def __repr__(self):
        return f'{self.gem_type}'
