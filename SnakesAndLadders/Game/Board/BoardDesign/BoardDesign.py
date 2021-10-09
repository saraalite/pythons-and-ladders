class BoardDesign:
    def __init__(self):
        self.board_width_in_squares: int = 10
        self.board_height_in_squares: int = 10

    def get_board_width_in_squares(self) -> int:
        return self.board_width_in_squares

    def get_board_height_in_squares(self) -> int:
        return self.board_height_in_squares
