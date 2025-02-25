"""
Splendor Board Game: Board Module

This module defines the Board component of the Splendor board game using the Kivy framework.

Classes:
- ImageButton: Represents a clickable image button of a token, used for game interaction.
- Board: Represents the game board and manages its state and appearance.

Functions:
- find_index: Finds the index of a target value in a matrix.
- find_common_elements: Finds common elements among multiple lists.
- get_opposite_diagonal: Calculates opposite diagonal cells between two given cells.

Note: This code assumes that the Token, GemType, and other necessary classes are already defined in separate modules.

"""

from kivy.graphics import Rectangle, Color
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.relativelayout import RelativeLayout

from models.unit.token import Token, GemType


def find_index(target_value, matrix):
    """
    Find the index of a target value in a matrix.

    Args:
    - target_value (int): The value to find in the matrix.
    - matrix (list of lists): The matrix to search for the target value.

    Yields:
    - tuple: The row and column indices of the target value in the matrix.
    """
    for row_index, row in enumerate(matrix):
        try:
            column_index = row.index(target_value)
        except ValueError:
            continue
        yield row_index, column_index


def find_common_elements(*lists_with_board):
    """
    Find common elements among multiple lists.

    Args:
    - *lists_with_board (list of lists): Lists containing elements to find common elements.

    Returns:
    - list: List of common elements found in the input lists.
    """
    lists = lists_with_board[1:]
    if not lists:
        return []

    # Convert each list to a set
    sets = [set(lst) for lst in lists]

    # Find the intersection of all sets
    common_elements = set.intersection(*sets)

    return list(common_elements)


def get_opposite_diagonal(cell1, cell2):
    """
    Calculate opposite diagonal cells between two given cells.

    Args:
    - cell1 (tuple): Row and column indices of the first cell.
    - cell2 (tuple): Row and column indices of the second cell.

    Returns:
    - tuple: Two tuples representing opposite diagonal cells.
    """
    row1, col1 = cell1
    row2, col2 = cell2

    opposite1 = (row1 - (row2 - row1), col1 - (col2 - col1))
    opposite2 = (row2 + (row2 - row1), col2 + (col2 - col1))

    return opposite1, opposite2


class ImageButton(ButtonBehavior, Image):
    """
    Represents a clickable image button containing a token, used for game interaction.

    Attributes:
    - row (int): Row index of the button on the game board.
    - col (int): Column index of the button on the game board.
    - current_size (tuple): The current size of the button.

    Methods:
    - on_press: Event handler for button press.
    - click_when_choosing_token: Event handler for button press when choosing a token on the board (when picking a card
        containing the special effect: 'take same color').
    - click_when_turn: Event handler for button press during a player's turn.
    """

    def __init__(self, row, col, **kwargs):
        """
        Initialize the ImageButton.

        Args:
        - row (int): Row index of the button on the game board.
        - col (int): Column index of the button on the game board.
        - **kwargs: Additional keyword arguments.
        """
        super(ImageButton, self).__init__(**kwargs)
        self.current_size = self.size
        self.row = row
        self.col = col

    def on_press(self):
        """
        Event handler for button press.

        Depending on the game state, calls either click_when_choosing_token or click_when_turn.
        """
        if self.parent.parent.parent.choosing_token_on_board:
            self.click_when_choosing_token()
        else:
            self.click_when_turn()

    def click_when_choosing_token(self):
        """
        Event handler for button press when choosing a token on the board.

        Checks if the clicked cell is one of the available token choices and takes special effects accordingly.
        """
        current_cell = [self.row, self.col]
        if current_cell in self.parent.indexes_tokens_to_choose:
            self.parent.take_token_special_effect(current_cell)

    def click_when_turn(self):
        """
        Event handler for button press during a player's turn.

        Handles the logic for selecting and confirming cells during a turn.
        """
        current_cell = (self.row, self.col)
        current_gemtype = self.parent.board_gems[self.row][self.col].gem_type

        if current_cell in self.parent.clicked_cells:
            if len(self.parent.clicked_cells) == 3:
                cells = zip(*self.parent.clicked_cells)
                middle_cell = tuple(sum(coord) // 3 for coord in cells)

                if current_cell != middle_cell:
                    click_index = self.parent.clicked_cells.index(current_cell)
                    del self.parent.clicked_cells[click_index]
                    del self.parent.clicked_cells_gemtype[click_index]
            else:
                click_index = self.parent.clicked_cells.index(current_cell)
                del self.parent.clicked_cells[click_index]
                del self.parent.clicked_cells_gemtype[click_index]

        elif current_cell in self.parent.not_clickable_cells_index or current_gemtype == GemType.ANY:
            pass
        else:
            self.parent.clicked_cells.append(current_cell)
            self.parent.cell_size = self.size
            self.parent.width_confirm_cell = self.parent.cell_size[0] * .4
            self.parent.height_confirm_cell = self.parent.cell_size[1] * .4
            self.parent.clicked_cells_gemtype.append(self.parent.board_gems[self.row][self.col])

        self.parent.update_board()


class Board(RelativeLayout):
    """
    Represents the game board and manages its state and appearance.

    Attributes:
    - cols (int): Number of columns in the game board.
    - rows (int): Number of rows in the game board.
    - clicked_cells (list of tuples): List of currently clicked cells during a turn.
    - clicked_cells_gemtype (list): List of gem types corresponding to clicked cells.
    - not_clickable_cells_pos (list of tuples): List of positions for cells that are not clickable.
    - not_clickable_cells_index (list of tuples): List of indices for cells that are not clickable.
    - confirm_pos (tuple): Position for the confirmation button.
    - indexes_tokens_to_choose (list of tuples): Indices of tokens available for choosing (when picking a card with the
        special effect 'take same color').
    - cell_size (tuple): Size of each cell on the game board (width, height).
    - index_board (list of lists): Matrix representing the order of filling of cells on the game board.
    - board_gems (list of lists): Matrix representing the gem types of cells on the game board.

    Methods:
    - fill: Fill the game board with tokens from the token bag.
    - update_board: Update the visual appearance of the game board.
    - draw_board: Draw the game board with gem images.
    - color_clicked_cells: Color the cells that are currently clicked during a turn.
    - color_not_clickable_cells: Color the cells that are not clickable during a turn.
    - color_cells_to_choose: Color the cells containing tokens available for choosing.
    - color_cells_to_not_choose: Color the cells that do not contain tokens available for choosing.
    - generate_not_clickable_cells: Generate lists of not-clickable cells based on the current selection.
    - generate_not_clickable_cells_one_selected: Generate not-clickable cells logic for one selected cell.
    - generate_not_clickable_cells_one_selected_gold: Generate not-clickable cells logic for one selected gold cell.
    - generate_not_clickable_cells_two_selected: Generate not-clickable cells logic for two selected cells.
    - generate_not_clickable_cells_three_selected: Generate not-clickable cells logic for three selected cells.
    - get_confirmation_index: Get the position for the confirmation button based on the selected cells.
    - add_confirmation_to_pick: Add the confirmation button to the game board.
    - confirmation_button_pressed: Event handler for the confirmation button press.
    - take_token_special_effect: Handle special effects when choosing a token from the board.
    - on_window_resize: Event handler for window resize.
    """

    def __init__(self, tokenbag=None, **kwargs):
        """
        Initializes the Board object.

        Args:
        - tokenbag: An token bag to fill the board with tokens.
        - **kwargs: Additional keyword arguments.
        """
        super(Board, self).__init__(**kwargs)
        self.bind(size=self.on_window_resize)
        self.cols = 5
        self.rows = 5

        self.clicked_cells = []
        self.clicked_cells_gemtype = []
        self.not_clickable_cells_pos = []
        self.not_clickable_cells_index = []
        self.confirm_pos = None

        self.indexes_tokens_to_choose = []

        self.popup_reserve = None

        self.cell_size = (self.width / self.cols, self.height / self.rows)

        self.index_board = [
            [21, 22, 23, 24, 25],
            [20, 7, 8, 9, 10],
            [19, 6, 1, 2, 11],
            [18, 5, 4, 3, 12],
            [17, 16, 15, 14, 13]
        ]
        self.board_gems = [[Token(gem_type=GemType.ANY)] * 5 for _ in range(5)]

        self.fill(tokenbag)

    def fill(self, tokenbag=None):
        """
        Fill the game board with tokens from the token bag.

        Args:
        - tokenbag: An optional token bag to fill the board with tokens.
        """
        for current_position in range(1, 26):
            if tokenbag.get_number_of_tokens_in_bag() > 0:
                matches = [match for match in find_index(current_position, self.index_board)]
                double_index = list(matches[0])
                if self.board_gems[double_index[0]][double_index[1]].gem_type == GemType.ANY:
                    token = tokenbag.tokens.pop(0)
                    self.board_gems[double_index[0]][double_index[1]] = token
        self.update_board()

    def update_board(self, indexes_tokens_to_choose=None, *args):
        """
        Update the visual appearance of the game board.

        Args:
        - indexes_tokens_to_choose: Indices of tokens available for choosing.
        - *args: Additional arguments.
        """
        self.clear_widgets()
        self.canvas.clear()
        self.draw_board()
        if self.parent is None:
            return
        if self.parent.parent.choosing_token_on_board:
            self.indexes_tokens_to_choose = indexes_tokens_to_choose
            self.color_cells_to_choose()
            self.color_cells_to_not_choose()
        else:
            self.color_clicked_cells()
            self.generate_not_clickable_cells()
            self.color_not_clickable_cells()
            if len(self.clicked_cells) > 0:
                self.get_confirmation_index()
                self.add_confirmation_to_pick()

    def draw_board(self):
        """ Draw the game board with gem images. """
        for row in range(len(self.board_gems)):
            for col in range(len(self.board_gems[row])):
                if isinstance(self.board_gems[row][col], Token):
                    image = ImageButton(
                        row=row,
                        col=col,
                        source=Token(self.board_gems[row][col].gem_type).image,
                        fit_mode='cover'
                    )
                    image.size_hint = (None, None)
                    image.size = (self.width / self.cols, self.height / self.rows)
                    image.pos = (col * image.width, (self.rows - 1 - row) * image.height)
                    self.add_widget(image)

    def color_clicked_cells(self):
        """ Color the cells that are currently clicked during a turn. """
        for clicked_cell in self.clicked_cells:
            cell_pos_x = clicked_cell[1] * self.cell_size[0]
            cell_pos_y = (4 - clicked_cell[0]) * self.cell_size[1]
            with self.canvas:
                Color(0, 1, 0, .5, mode='rgba')
                Rectangle(pos=(cell_pos_x, cell_pos_y), size=self.cell_size)

    def color_not_clickable_cells(self):
        """ Color the cells that are not clickable during a turn. """
        for coord_to_darken in self.not_clickable_cells_pos:
            with self.canvas:
                Color(0, 0, 0, .5, mode='rgba')
                Rectangle(pos=coord_to_darken, size=self.cell_size)

    def color_cells_to_choose(self):
        """ Color the cells containing tokens available for choosing. """
        for index in self.indexes_tokens_to_choose:
            cell_pos_x = index[1] * self.cell_size[0]
            cell_pos_y = (4 - index[0]) * self.cell_size[1]
            with self.canvas:
                Color(0, 1, 0, .5, mode='rgba')
                Rectangle(pos=(cell_pos_x, cell_pos_y), size=self.cell_size)

    def color_cells_to_not_choose(self):
        """ Color the cells that do not contain tokens available for choosing. """
        for possible_row in range(5):
            for possible_col in range(5):
                if [possible_row, possible_col] not in self.indexes_tokens_to_choose:
                    cell_pos_x = possible_col * self.cell_size[0]
                    cell_pos_y = (4 - possible_row) * self.cell_size[1]
                    with self.canvas:
                        Color(0, 0, 0, .5, mode='rgba')
                        Rectangle(pos=(cell_pos_x, cell_pos_y), size=self.cell_size)

    def generate_not_clickable_cells(self):
        """ Generate lists of not-clickable cells based on the current selection. """
        self.not_clickable_cells_pos = []
        self.not_clickable_cells_index = []
        if len(self.clicked_cells) == 1:
            if self.clicked_cells_gemtype[0].gem_type == GemType.GOLD:
                self.generate_not_clickable_cells_one_selected_gold()
            else:
                self.generate_not_clickable_cells_one_selected()
        elif len(self.clicked_cells) == 2:
            self.generate_not_clickable_cells_two_selected()
        elif len(self.clicked_cells) == 3:
            self.generate_not_clickable_cells_three_selected()

    def generate_not_clickable_cells_one_selected(self):
        """ Generate not-clickable cells logic for one selected cell. """
        clicked_cell = self.clicked_cells[0]
        for possible_row in range(5):
            for possible_col in range(5):
                # If the cell it at more than one cell than the clicked one
                # Or the cell is a Gold token
                # Or the cell is empty
                if (
                        abs(clicked_cell[0] - possible_row) > 1 or abs(clicked_cell[1] - possible_col) > 1 or
                        self.board_gems[possible_row][possible_col].gem_type == GemType.GOLD or
                        self.board_gems[possible_row][possible_col].gem_type == GemType.ANY
                ):
                    cell_pos_x = possible_col * self.cell_size[0]
                    cell_pos_y = (4 - possible_row) * self.cell_size[1]

                    self.not_clickable_cells_pos.append((cell_pos_x, cell_pos_y))
                    self.not_clickable_cells_index.append((possible_row, possible_col))

    def generate_not_clickable_cells_one_selected_gold(self):
        """ Generate not-clickable cells logic for one selected gold cell. """
        clicked_cell = self.clicked_cells[0]
        for possible_row in range(5):
            for possible_col in range(5):
                if possible_row != clicked_cell[0] or possible_col != clicked_cell[1]:
                    cell_pos_x = possible_col * self.cell_size[0]
                    cell_pos_y = (4 - possible_row) * self.cell_size[1]

                    self.not_clickable_cells_pos.append((cell_pos_x, cell_pos_y))
                    self.not_clickable_cells_index.append((possible_row, possible_col))

    def generate_not_clickable_cells_two_selected(self):
        """ Generate not-clickable cells logic for two selected cells. """
        clicked_one = self.clicked_cells[0]
        clicked_two = self.clicked_cells[1]
        possible_clicks = []

        # If the two clicks are in a vertical line
        if clicked_one[1] == clicked_two[1]:
            possible_clicks.append((min(clicked_one[0], clicked_two[0]) - 1, clicked_one[1]))
            possible_clicks.append((max(clicked_one[0], clicked_two[0]) + 1, clicked_one[1]))
        # If the two clicks are in a horizontal line
        if clicked_one[0] == clicked_two[0]:
            possible_clicks.append((clicked_one[0], min(clicked_one[1], clicked_two[1]) - 1))
            possible_clicks.append((clicked_one[0], max(clicked_one[1], clicked_two[1]) + 1))
        else:
            opposites = get_opposite_diagonal(clicked_one, clicked_two)
            for cell in opposites:
                possible_clicks.append(cell)

        for possible_row in range(5):
            for possible_col in range(5):
                cell_position = (possible_col * self.cell_size[0], (4 - possible_row) * self.cell_size[1])
                cell_index = (possible_row, possible_col)

                # If the cell is not in the clicks that are authorized or that the Token is not a gold one
                # And if the cell is not clicked
                if ((
                        cell_index not in possible_clicks or
                        self.board_gems[possible_row][possible_col].gem_type == GemType.GOLD or
                        self.board_gems[possible_row][possible_col].gem_type == GemType.ANY
                ) and
                        cell_index not in self.clicked_cells):
                    self.not_clickable_cells_pos.append(cell_position)
                    self.not_clickable_cells_index.append(cell_index)

    def generate_not_clickable_cells_three_selected(self):
        """ Generate not-clickable cells logic for three selected cells. """
        for possible_row in range(5):
            for possible_col in range(5):
                if (possible_row, possible_col) not in self.clicked_cells:
                    cell_pos_x = possible_col * self.cell_size[0]
                    cell_pos_y = (4 - possible_row) * self.cell_size[1]
                    self.not_clickable_cells_pos.append((cell_pos_x, cell_pos_y))
                    self.not_clickable_cells_index.append((possible_row, possible_col))

    def get_confirmation_index(self):
        """ Get the position for the confirmation button based on the selected cells. """
        righteous_cell = [0, 0]
        for cell in self.clicked_cells:
            if cell[1] >= righteous_cell[1]:
                righteous_cell = cell
        if righteous_cell[1] == 4:
            still_going_left = True
            y_index_empty = 0
            while still_going_left:
                if (righteous_cell[0], righteous_cell[1] - y_index_empty) in self.clicked_cells:
                    y_index_empty += 1
                else:
                    still_going_left = False
            confirm_x = (righteous_cell[1] - y_index_empty + 1) * self.cell_size[0] - self.width_confirm_cell
            confirm_y = (4 - righteous_cell[0]) * self.cell_size[1]
            self.confirm_pos = (confirm_x, confirm_y)
        else:
            confirm_x = (righteous_cell[1] * self.cell_size[0]) + self.cell_size[0]
            confirm_y = (4 - righteous_cell[0]) * self.cell_size[1]
            self.confirm_pos = (confirm_x, confirm_y)

    def add_confirmation_to_pick(self):
        """ Add the confirmation button to the game board. """
        confirmation_button = Button(
            pos=(self.confirm_pos[0], self.confirm_pos[1]),
            size_hint=(None, None),
            size=(self.width_confirm_cell, self.height_confirm_cell)
        )
        confirmation_button.bind(on_press=self.confirmation_button_pressed)
        self.add_widget(confirmation_button)

    def confirmation_button_pressed(self, instance):
        """
        Event handler for the confirmation button press.

        Args:
        - instance: The instance of the confirmation button.
        """
        if self.clicked_cells_gemtype[0].gem_type == GemType.GOLD:
            level_cards_dict = {'1': self.parent.parent.middleboard.displayed_cards1.cards,
                                '2': self.parent.parent.middleboard.displayed_cards2.cards,
                                '3': self.parent.parent.middleboard.displayed_cards3.cards}
            self.popup_reserve = ReserveCardPopup(level_cards_dict=level_cards_dict, caller_board=self)
            self.popup_reserve.bind(on_dismiss=self.after_popup_closed)
            self.popup_reserve.open()
        else:
            self.continue_after_popup()

    def after_popup_closed(self, instance):
        """
        Callback function to be called when the popup is closed.

        Args:
        - instance: The instance of the popup.
        """
        if instance.dismissed_by_button:
            self.continue_after_popup()
        else:
            pass

    def continue_after_popup(self):
        """
        Continues the game logic after the popup is closed.
        """
        self.parent.parent.current_player.owned_tokens.add_tokens(self.clicked_cells_gemtype)
        for position in self.clicked_cells:
            self.board_gems[position[0]][position[1]].gem_type = GemType.ANY
        self.not_clickable_cells_pos = []
        self.not_clickable_cells_index = []
        self.clicked_cells = []
        self.clicked_cells_gemtype = []
        self.confirm_pos = None
        self.update_board()

        self.parent.parent.end_turn()

    def take_token_special_effect(self, chose_cell=None):
        """
        Handle choosing a token from the board when the special effect 'take same color' is used.

        Args:
        - chose_cell: The selected cell for choosing a token.
        """
        color_to_take = self.board_gems[chose_cell[0]][chose_cell[1]].gem_type
        self.parent.parent.current_player.owned_tokens.add_token(color_to_take)
        self.board_gems[chose_cell[0]][chose_cell[1]].gem_type = GemType.ANY
        self.indexes_tokens_to_choose = []
        self.parent.parent.current_player.owned_cards.get_card_widget(color_to_take).after_special_effect()
        self.parent.parent.choosing_token_on_board = False
        self.update_board()

    def on_window_resize(self, instance, value):
        """
        Event handler for window resize.

        Args:
        - instance: The instance triggering the event.
        - value: The new value after the resize.
        """
        self.update_board()


class ReserveCardPopupBoxPerLevelCardsButton(Button):
    def __init__(self, card=None, caller_board=None, **kwargs):
        super(ReserveCardPopupBoxPerLevelCardsButton, self).__init__(**kwargs)
        self.card = card
        self.caller_board = caller_board
        self.text = self.get_card_text()

    def get_card_text(self):
        return (
            f'ID: {self.card.card_id}\n'
            f'Color: {self.card.value} {self.card.color}\n'
            f'Victory points: {self.card.victory_points}\n'
            f'Crowns: {self.card.crowns}\n'
            f'Special effect: {self.card.special_effect}\n\n'
            f'Cost:\n{self.display_cost()}\n'
        )

    def display_cost(self):
        return '\n'.join([f'- {color}: {value}' for color, value in self.card.cost.items()])

    def on_press(self):
        self.caller_board.popup_reserve.dismissed_by_button = True
        # add card to current player's reserved cards
        self.caller_board.parent.parent.current_player.reserved_cards.reserved_cards.append(self.card)
        self.caller_board.parent.parent.current_player.reserved_cards.show_reserved_cards()
        self.caller_board.popup_reserve.dismiss()
        # self.parent.parent.parent.parent.parent.parent.parent.parent.current_player.reserved_cards.append(self.card)


class ReserveCardPopupBoxPerLevelCards(BoxLayout):
    def __init__(self, cards=None, caller_board=None, **kwargs):
        super(ReserveCardPopupBoxPerLevelCards, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.cards = cards
        self.card = None
        self.caller_board = caller_board
        self.build_ui()

    def build_ui(self):
        for card in self.cards:
            self.card = card
            players_tokens = self.caller_board.parent.parent.current_player.get_total_color()
            self.add_widget(ReserveCardPopupBoxPerLevelCardsButton(card=self.card, caller_board=self.caller_board))


class ReserveCardPopupBoxPerLevel(BoxLayout):
    def __init__(self, level_cards_dict=None, caller_board=None, **kwargs):
        super(ReserveCardPopupBoxPerLevel, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.level_cards_dict = level_cards_dict
        self.caller_board = caller_board
        self.build_ui()

    def build_ui(self):
        for level, cards in self.level_cards_dict.items():
            self.add_widget(Label(text=f'Level {level}'))
            self.add_widget(ReserveCardPopupBoxPerLevelCards(cards=cards, caller_board=self.caller_board))


class ReserveCardPopup(Popup):
    """
    A popup window for displaying cards of all levels when a gold token is chosen.

    Attributes:
    """
    def __init__(self, level_cards_dict=None, caller_board=None, **kwargs):
        super(ReserveCardPopup, self).__init__(**kwargs)
        self.dismissed_by_button = False
        self.title = f'Reserve a card'
        self.size_hint = (.8, .8)
        self.level_cards_dict = level_cards_dict
        popup_card = ReserveCardPopupBoxPerLevel(level_cards_dict=self.level_cards_dict, caller_board=caller_board)
        self.add_widget(popup_card)
