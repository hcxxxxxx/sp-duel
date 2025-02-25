from models.unit.card import Card, SpecialEffect
from models.unit.token import GemType

LEVEL1_CARDS = [
    Card(
        card_id='1',
        level=1,
        cost={GemType.GREEN: 2, GemType.RED: 2},
        value=1,
        color=GemType.BLACK,
        crowns=0,
        victory_points=0,
        special_effect=SpecialEffect.TAKE_SAME_COLOR
    ),
    Card(
        card_id='2',
        level=1,
        cost={GemType.WHITE: 2, GemType.BLUE: 2, GemType.PEARL: 1},
        value=1,
        color=GemType.BLACK,
        crowns=0,
        victory_points=0,
        special_effect=SpecialEffect.PLAY_AGAIN
    ),
    Card(
        card_id='3',
        level=1,
        cost={GemType.WHITE: 3},
        value=1,
        color=GemType.BLACK,
        crowns=1,
        victory_points=0,
        special_effect=None
    ),
    Card(
        card_id='4',
        level=1,
        cost={GemType.WHITE: 3, GemType.BLACK: 2},
        value=1,
        color=GemType.GREEN,
        crowns=0,
        victory_points=1,
        special_effect=None
    ),
    Card(
        card_id='5',
        level=1,
        cost={GemType.RED: 2, GemType.BLACK: 2, GemType.PEARL: 1},
        value=1,
        color=GemType.GREEN,
        crowns=0,
        victory_points=0,
        special_effect=SpecialEffect.PLAY_AGAIN
    ),
    Card(
        card_id='6',
        level=1,
        cost={GemType.WHITE: 2, GemType.BLUE: 2},
        value=1,
        color=GemType.GREEN,
        crowns=0,
        victory_points=0,
        special_effect=SpecialEffect.TAKE_SAME_COLOR
    ),
    Card(
        card_id='7',
        level=1,
        cost={GemType.BLACK: 4, GemType.PEARL: 1},
        value=1,
        color=GemType.ANY,
        crowns=0,
        victory_points=1,
        special_effect=None
    ),
    Card(
        card_id='8',
        level=1,
        cost={GemType.BLACK: 3},
        value=1,
        color=GemType.RED,
        crowns=1,
        victory_points=0,
        special_effect=None
    ),
    Card(
        card_id='9',
        level=1,
        cost={GemType.WHITE: 2, GemType.BLACK: 2, GemType.PEARL: 1},
        value=1,
        color=GemType.RED,
        crowns=0,
        victory_points=0,
        special_effect=SpecialEffect.PLAY_AGAIN
    ),
    Card(
        card_id='10',
        level=1,
        cost={GemType.BLACK: 2, GemType.WHITE: 2},
        value=1,
        color=GemType.BLUE,
        crowns=0,
        victory_points=0,
        special_effect=SpecialEffect.TAKE_SAME_COLOR
    ),
    Card(
        card_id='11',
        level=1,
        cost={GemType.BLACK: 3, GemType.RED: 2},
        value=1,
        color=GemType.BLUE,
        crowns=0,
        victory_points=1,
        special_effect=None
    ),
    Card(
        card_id='12',
        level=1,
        cost={GemType.GREEN: 3},
        value=1,
        color=GemType.BLUE,
        crowns=1,
        victory_points=0,
        special_effect=None
    ),
    Card(
        card_id='13',
        level=1,
        cost={GemType.BLACK: 2, GemType.RED: 2},
        value=1,
        color=GemType.WHITE,
        crowns=0,
        victory_points=0,
        special_effect=SpecialEffect.TAKE_SAME_COLOR
    ),
    Card(
        card_id='14',
        level=1,
        cost={GemType.BLUE: 1, GemType.GREEN: 1, GemType.RED: 1, GemType.BLACK: 1},
        value=1,
        color=GemType.WHITE,
        crowns=0,
        victory_points=0,
        special_effect=None
    ),
    Card(
        card_id='15',
        level=1,
        cost={GemType.BLUE: 1, GemType.WHITE: 1, GemType.RED: 1, GemType.BLACK: 1},
        value=1,
        color=GemType.GREEN,
        crowns=0,
        victory_points=0,
        special_effect=None
    ),
    Card(
        card_id='16',
        level=1,
        cost={GemType.BLUE: 1, GemType.GREEN: 1, GemType.RED: 1, GemType.WHITE: 1},
        value=1,
        color=GemType.BLACK,
        crowns=0,
        victory_points=0,
        special_effect=None
    ),
    Card(
        card_id='17',
        level=1,
        cost={GemType.BLUE: 1, GemType.GREEN: 1, GemType.WHITE: 1, GemType.BLACK: 1},
        value=1,
        color=GemType.RED,
        crowns=0,
        victory_points=0,
        special_effect=None
    ),
    Card(
        card_id='18',
        level=1,
        cost={GemType.WHITE: 1, GemType.GREEN: 1, GemType.RED: 1, GemType.BLACK: 1},
        value=1,
        color=GemType.BLUE,
        crowns=0,
        victory_points=0,
        special_effect=None
    ),
    Card(
        card_id='19',
        level=1,
        cost={GemType.RED: 3, GemType.GREEN: 2},
        value=1,
        color=GemType.WHITE,
        crowns=0,
        victory_points=1,
        special_effect=None
    ),
    Card(
        card_id='20',
        level=1,
        cost={GemType.GREEN: 3, GemType.BLUE: 2},
        value=1,
        color=GemType.BLACK,
        crowns=0,
        victory_points=1,
        special_effect=None
    ),
    Card(
        card_id='21',
        level=1,
        cost={GemType.BLUE: 3, GemType.WHITE: 2},
        value=1,
        color=GemType.RED,
        crowns=0,
        victory_points=1,
        special_effect=None
    ),
    Card(
        card_id='22',
        level=1,
        cost={GemType.BLUE: 2, GemType.GREEN: 2},
        value=1,
        color=GemType.RED,
        crowns=0,
        victory_points=0,
        special_effect=SpecialEffect.TAKE_SAME_COLOR
    ),
    Card(
        card_id='23',
        level=1,
        cost={GemType.BLUE: 3},
        value=1,
        color=GemType.WHITE,
        crowns=1,
        victory_points=0,
        special_effect=None
    ),
    Card(
        card_id='24',
        level=1,
        cost={GemType.RED: 3},
        value=1,
        color=GemType.GREEN,
        crowns=1,
        victory_points=0,
        special_effect=None
    ),
    Card(
        card_id='25',
        level=1,
        cost={GemType.BLUE: 2, GemType.GREEN: 2, GemType.PEARL: 1},
        value=1,
        color=GemType.WHITE,
        crowns=0,
        victory_points=0,
        special_effect=SpecialEffect.PLAY_AGAIN
    ),
    Card(
        card_id='26',
        level=1,
        cost={GemType.GREEN: 2, GemType.RED: 2, GemType.PEARL: 1},
        value=1,
        color=GemType.BLUE,
        crowns=0,
        victory_points=0,
        special_effect=SpecialEffect.PLAY_AGAIN
    ),
    Card(
        card_id='27',
        level=1,
        cost={GemType.BLUE: 2, GemType.RED: 2, GemType.BLACK: 1, GemType.PEARL: 1},
        value=1,
        color=GemType.ANY,
        crowns=0,
        victory_points=1,
        special_effect=None
    ),
    Card(
        card_id='28',
        level=1,
        cost={GemType.WHITE: 4, GemType.PEARL: 1},
        value=1,
        color=GemType.ANY,
        crowns=1,
        victory_points=0,
        special_effect=None
    ),
    Card(
        card_id='29',
        level=1,
        cost={GemType.WHITE: 2, GemType.GREEN: 2, GemType.BLACK: 1, GemType.PEARL: 1},
        value=1,
        color=GemType.ANY,
        crowns=0,
        victory_points=1,
        special_effect=None
    ),
    Card(
        card_id='30',
        level=1,
        cost={GemType.RED: 4, GemType.PEARL: 1},
        value=0,
        color=None,
        crowns=0,
        victory_points=3,
        special_effect=None
    ),
]

LEVEL2_CARDS = [
    Card(
        card_id='31',
        level=2,
        cost={GemType.WHITE: 2, GemType.BLUE: 2, GemType.GREEN: 2, GemType.PEARL: 1},
        value=1,
        color=GemType.RED,
        crowns=1,
        victory_points=2,
        special_effect=None
    ),
    Card(
        card_id='32',
        level=2,
        cost={GemType.WHITE: 2, GemType.BLUE: 2, GemType.BLACK: 2, GemType.PEARL: 1},
        value=1,
        color=GemType.GREEN,
        crowns=1,
        victory_points=2,
        special_effect=None
    ),
    Card(
        card_id='33',
        level=2,
        cost={GemType.WHITE: 2, GemType.RED: 2, GemType.BLACK: 2, GemType.PEARL: 1},
        value=1,
        color=GemType.BLUE,
        crowns=1,
        victory_points=2,
        special_effect=None
    ),
    Card(
        card_id='34',
        level=2,
        cost={GemType.RED: 2, GemType.BLUE: 2, GemType.GREEN: 2, GemType.PEARL: 1},
        value=1,
        color=GemType.BLACK,
        crowns=1,
        victory_points=2,
        special_effect=None
    ),
    Card(
        card_id='35',
        level=2,
        cost={GemType.RED: 2, GemType.BLACK: 2, GemType.GREEN: 2, GemType.PEARL: 1},
        value=1,
        color=GemType.WHITE,
        crowns=1,
        victory_points=2,
        special_effect=None
    ),
    Card(
        card_id='36',
        level=2,
        cost={GemType.GREEN: 6, GemType.PEARL: 1},
        value=1,
        color=GemType.ANY,
        crowns=2,
        victory_points=0,
        special_effect=None
    ),
    Card(
        card_id='37',
        level=2,
        cost={GemType.BLUE: 6, GemType.PEARL: 1},
        value=1,
        color=GemType.ANY,
        crowns=2,
        victory_points=0,
        special_effect=None
    ),
    Card(
        card_id='38',
        level=2,
        cost={GemType.GREEN: 6, GemType.PEARL: 1},
        value=1,
        color=GemType.ANY,
        crowns=0,
        victory_points=2,
        special_effect=None
    ),
    Card(
        card_id='39',
        level=2,
        cost={GemType.BLACK: 5, GemType.WHITE: 2},
        value=2,
        color=GemType.RED,
        crowns=0,
        victory_points=1,
        special_effect=None
    ),
    Card(
        card_id='40',
        level=2,
        cost={GemType.GREEN: 5, GemType.RED: 2},
        value=2,
        color=GemType.BLUE,
        crowns=0,
        victory_points=1,
        special_effect=None
    ),
    Card(
        card_id='41',
        level=2,
        cost={GemType.BLUE: 5, GemType.GREEN: 2},
        value=2,
        color=GemType.WHITE,
        crowns=0,
        victory_points=1,
        special_effect=None
    ),
    Card(
        card_id='42',
        level=2,
        cost={GemType.WHITE: 5, GemType.BLUE: 2},
        value=2,
        color=GemType.BLACK,
        crowns=0,
        victory_points=1,
        special_effect=None
    ),
    Card(
        card_id='43',
        level=2,
        cost={GemType.RED: 5, GemType.BLACK: 2},
        value=2,
        color=GemType.GREEN,
        crowns=0,
        victory_points=1,
        special_effect=None
    ),
    Card(
        card_id='44',
        level=2,
        cost={GemType.BLUE: 4, GemType.RED: 3},
        value=1,
        color=GemType.WHITE,
        crowns=0,
        victory_points=1,
        special_effect=SpecialEffect.TAKE_OPPONENT_TOKEN
    ),
    Card(
        card_id='45',
        level=2,
        cost={GemType.RED: 4, GemType.WHITE: 3},
        value=1,
        color=GemType.GREEN,
        crowns=0,
        victory_points=1,
        special_effect=SpecialEffect.TAKE_OPPONENT_TOKEN
    ),
    Card(
        card_id='46',
        level=2,
        cost={GemType.BLACK: 4, GemType.BLUE: 3},
        value=1,
        color=GemType.RED,
        crowns=0,
        victory_points=1,
        special_effect=SpecialEffect.TAKE_OPPONENT_TOKEN
    ),
    Card(
        card_id='47',
        level=2,
        cost={GemType.GREEN: 4, GemType.BLACK: 3},
        value=1,
        color=GemType.BLUE,
        crowns=0,
        victory_points=1,
        special_effect=SpecialEffect.TAKE_OPPONENT_TOKEN
    ),
    Card(
        card_id='48',
        level=2,
        cost={GemType.WHITE: 4, GemType.GREEN: 3},
        value=1,
        color=GemType.BLACK,
        crowns=0,
        victory_points=1,
        special_effect=SpecialEffect.TAKE_OPPONENT_TOKEN
    ),
    Card(
        card_id='49',
        level=2,
        cost={GemType.RED: 4, GemType.GREEN: 2, GemType.PEARL: 1},
        value=1,
        color=GemType.RED,
        crowns=0,
        victory_points=2,
        special_effect=SpecialEffect.TAKE_SCROLL
    ),
    Card(
        card_id='50',
        level=2,
        cost={GemType.BLUE: 4, GemType.WHITE: 2, GemType.PEARL: 1},
        value=1,
        color=GemType.BLUE,
        crowns=0,
        victory_points=2,
        special_effect=SpecialEffect.TAKE_SCROLL
    ),
    Card(
        card_id='51',
        level=2,
        cost={GemType.GREEN: 4, GemType.BLUE: 2, GemType.PEARL: 1},
        value=1,
        color=GemType.GREEN,
        crowns=0,
        victory_points=2,
        special_effect=SpecialEffect.TAKE_SCROLL
    ),
    Card(
        card_id='52',
        level=2,
        cost={GemType.WHITE: 4, GemType.BLACK: 2, GemType.PEARL: 1},
        value=1,
        color=GemType.WHITE,
        crowns=0,
        victory_points=2,
        special_effect=SpecialEffect.TAKE_SCROLL
    ),
    Card(
        card_id='53',
        level=2,
        cost={GemType.BLACK: 4, GemType.RED: 2, GemType.PEARL: 1},
        value=1,
        color=GemType.BLACK,
        crowns=0,
        victory_points=2,
        special_effect=SpecialEffect.TAKE_SCROLL
    ),
    Card(
        card_id='54',
        level=2,
        cost={GemType.BLUE: 6, GemType.PEARL: 1},
        value=0,
        color=None,
        crowns=0,
        victory_points=5,
        special_effect=None
    ),
]

LEVEL3_CARDS = [
    Card(
        card_id='55',
        level=3,
        cost={GemType.BLUE: 5, GemType.GREEN: 3, GemType.BLACK: 3, GemType.PEARL: 1},
        value=1,
        color=GemType.RED,
        crowns=2,
        victory_points=3,
        special_effect=None
    ),
    Card(
        card_id='56',
        level=3,
        cost={GemType.RED: 5, GemType.BLUE: 3, GemType.BLACK: 3, GemType.PEARL: 1},
        value=1,
        color=GemType.WHITE,
        crowns=2,
        victory_points=3,
        special_effect=None
    ),
    Card(
        card_id='57',
        level=3,
        cost={GemType.WHITE: 5, GemType.BLUE: 3, GemType.RED: 3, GemType.PEARL: 1},
        value=1,
        color=GemType.GREEN,
        crowns=2,
        victory_points=3,
        special_effect=None
    ),
    Card(
        card_id='58',
        level=3,
        cost={GemType.GREEN: 5, GemType.WHITE: 3, GemType.RED: 3, GemType.PEARL: 1},
        value=1,
        color=GemType.BLACK,
        crowns=2,
        victory_points=3,
        special_effect=None
    ),
    Card(
        card_id='59',
        level=3,
        cost={GemType.BLACK: 5, GemType.GREEN: 3, GemType.WHITE: 3, GemType.PEARL: 1},
        value=1,
        color=GemType.BLUE,
        crowns=2,
        victory_points=3,
        special_effect=None
    ),
    Card(
        card_id='60',
        level=3,
        cost={GemType.BLACK: 8},
        value=1,
        color=GemType.ANY,
        crowns=3,
        victory_points=0,
        special_effect=None
    ),
    Card(
        card_id='61',
        level=3,
        cost={GemType.RED: 8},
        value=1,
        color=GemType.ANY,
        crowns=0,
        victory_points=3,
        special_effect=SpecialEffect.PLAY_AGAIN
    ),
    Card(
        card_id='62',
        level=3,
        cost={GemType.GREEN: 6, GemType.BLUE: 2, GemType.RED: 2},
        value=1,
        color=GemType.GREEN,
        crowns=0,
        victory_points=4,
        special_effect=None
    ),
    Card(
        card_id='63',
        level=3,
        cost={GemType.RED: 6, GemType.GREEN: 2, GemType.BLACK: 2},
        value=1,
        color=GemType.RED,
        crowns=0,
        victory_points=4,
        special_effect=None
    ),
    Card(
        card_id='64',
        level=3,
        cost={GemType.BLUE: 6, GemType.WHITE: 2, GemType.GREEN: 2},
        value=1,
        color=GemType.BLUE,
        crowns=0,
        victory_points=4,
        special_effect=None
    ),
    Card(
        card_id='65',
        level=3,
        cost={GemType.BLACK: 6, GemType.WHITE: 2, GemType.RED: 2},
        value=1,
        color=GemType.BLACK,
        crowns=0,
        victory_points=4,
        special_effect=None
    ),
    Card(
        card_id='66',
        level=3,
        cost={GemType.WHITE: 6, GemType.BLUE: 2, GemType.BLACK: 2},
        value=1,
        color=GemType.WHITE,
        crowns=0,
        victory_points=4,
        special_effect=None
    ),
    Card(
        card_id='67',
        level=3,
        cost={GemType.WHITE: 8},
        value=0,
        color=None,
        crowns=0,
        victory_points=6,
        special_effect=None
    ),
]

CROWN_CARDS = [
    Card(
        card_id='68',
        level=4,
        cost={},
        value=0,
        color=None,
        crowns=0,
        victory_points=3,
        special_effect=None
    ),
    Card(
        card_id='69',
        level=4,
        cost={},
        value=0,
        color=None,
        crowns=0,
        victory_points=2,
        special_effect=SpecialEffect.TAKE_SCROLL
    ),
    Card(
        card_id='70',
        level=4,
        cost={},
        value=0,
        color=None,
        crowns=0,
        victory_points=2,
        special_effect=SpecialEffect.PLAY_AGAIN
    ),
    Card(
        card_id='71',
        level=4,
        cost={},
        value=0,
        color=None,
        crowns=0,
        victory_points=2,
        special_effect=SpecialEffect.TAKE_OPPONENT_TOKEN
    ),
]
