from .BoardDesign.BoardDesign import BoardDesign


class Board:
    def __init__(self):
        self.board_design: BoardDesign = BoardDesign()

    def get_board_design(self) -> BoardDesign:
        return self.board_design

    def is_win_position(self, position: int) -> bool:
        return False

    def get_next_position_based_on_dice_result(
        self, current_position: int, dice_result: int
    ):
        return 0
