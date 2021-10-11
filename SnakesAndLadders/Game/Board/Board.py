from .BoardDesign.BoardDesign import BoardDesign
from .Snake.Snake import Snake
from .Ladder.Ladder import Ladder


class Board:
    def __init__(self):
        self.board_design: BoardDesign = BoardDesign()
        snakes_config = [
            {
                "head_position": 16,
                "tail_position": 6,
            },
            {
                "head_position": 49,
                "tail_position": 11,
            },
            {
                "head_position": 46,
                "tail_position": 25,
            },
            {
                "head_position": 62,
                "tail_position": 19,
            },
            {
                "head_position": 64,
                "tail_position": 60,
            },
            {
                "head_position": 74,
                "tail_position": 53,
            },
            {
                "head_position": 89,
                "tail_position": 68,
            },
            {
                "head_position": 95,
                "tail_position": 75,
            },
            {
                "head_position": 92,
                "tail_position": 88,
            },
            {
                "head_position": 99,
                "tail_position": 80,
            },
        ]
        self.snakes: list[Snake] = []
        for snake_config in snakes_config:
            self.snakes.append(
                Snake(snake_config["head_position"], snake_config["tail_position"])
            )

        ladders_config = [
            {
                "bottom_position": 2,
                "top_position": 38,
            },
            {
                "bottom_position": 7,
                "top_position": 14,
            },
            {
                "bottom_position": 9,
                "top_position": 31,
            },
            {
                "bottom_position": 15,
                "top_position": 26,
            },
            {
                "bottom_position": 21,
                "top_position": 42,
            },
            {
                "bottom_position": 28,
                "top_position": 84,
            },
            {
                "bottom_position": 51,
                "top_position": 67,
            },
            {
                "bottom_position": 71,
                "top_position": 91,
            },
            {
                "bottom_position": 78,
                "top_position": 98,
            },
            {
                "bottom_position": 87,
                "top_position": 94,
            },
        ]
        self.ladders: list[Ladder] = []
        for ladder_config in ladders_config:
            self.ladders.append(
                Ladder(ladder_config["bottom_position"], ladder_config["top_position"])
            )

    def get_board_design(self) -> BoardDesign:
        return self.board_design

    def get_next_position_based_on_dice_result(
        self, current_position: int, dice_result: int
    ):
        next_position = current_position + dice_result
        if next_position > self.get_last_position_in_board():
            next_position = current_position

        next_position = self.get_next_position_tail_if_snake_head_reached(next_position)

        next_position = self.get_next_position_top_if_bottom_ladder_reached(
            next_position
        )

        return next_position

    def get_last_position_in_board(self) -> int:
        return (
            self.board_design.get_board_height_in_squares()
            * self.board_design.get_board_width_in_squares()
        )

    def get_next_position_tail_if_snake_head_reached(self, next_position) -> int:
        next_position_based_on_snakes = next_position

        for snake in self.snakes:
            if snake.get_head_position() == next_position:
                next_position_based_on_snakes = snake.get_tail_position()

        return next_position_based_on_snakes

    def get_next_position_top_if_bottom_ladder_reached(self, next_position) -> int:
        next_position_based_on_ladders = next_position

        for ladder in self.ladders:
            if ladder.get_bottom_position() == next_position:
                next_position_based_on_ladders = ladder.get_top_position()

        return next_position_based_on_ladders
