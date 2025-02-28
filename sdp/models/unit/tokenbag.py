from collections import Counter
from models.unit.token import GemType, Token
import random


class TokenBag:
    tokens = None

    def __init__(self):
        self.tokens = []
        gem_type_counts = {
            GemType.BLACK: 4,
            GemType.BLUE: 4,
            GemType.GREEN: 4,
            GemType.RED: 4,
            GemType.WHITE: 4,
            GemType.PEARL: 2,
            GemType.GOLD: 3,
        }

        for gem_type, count in gem_type_counts.items():
            self.tokens.extend([Token(gem_type) for _ in range(count)])

        self.shuffle()

    def shuffle(self):
        random.shuffle(self.tokens)

    def empty_bag_of_tokens(self):
        self.tokens = []

    def get_number_of_tokens_in_bag(self):
        return len(self.tokens)

    def add_tokens(self, player_tokens=None):
        self.tokens = dict(Counter(self.tokens) + Counter(player_tokens))

    def __str__(self):
        return f'{self.tokens}'
