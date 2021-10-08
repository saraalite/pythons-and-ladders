from SnakesAndLadders.Game.Game import Game
from SnakesAndLadders.Game.Player.Player import Player


class PrintGameWrapper:
    @staticmethod
    def print_game(game: Game):
        board_height_in_squares = (
            game.get_board().get_board_design().BOARD_HEIGHT_IN_SQUARES
        )
        board_width_in_squares = (
            game.get_board().get_board_design().BOARD_WIDTH_IN_SQUARES
        )

        PrintGameWrapper.print_bottom(board_width_in_squares)

        for squareY in range(1, board_height_in_squares + 1):
            PrintGameWrapper.print_side()
            PrintGameWrapper.print_row_with_content(
                squareY, board_width_in_squares, board_height_in_squares, game
            )
            PrintGameWrapper.print_bottom(board_width_in_squares)

    @staticmethod
    def players_token_is_in_position(position: int, player_list: "list[Player]"):
        players_string = ""
        for player in player_list:
            if player.get_player_token_position() == position:
                players_string += f"P{player.get_position_in_player_list()}"
        return players_string

    @staticmethod
    def print_bottom(board_width_in_squares):
        for squareX in range(1, board_width_in_squares + 1):
            print("--------", end="")
        print()

    def print_side():
        print("|", end="")

    @staticmethod
    def print_row_with_content(
        squareY: int,
        board_width_in_squares: int,
        board_height_in_squares: int,
        game: Game,
    ):
        for squareX in range(1, board_width_in_squares + 1):
            position_in_list = (
                PrintGameWrapper.get_position_in_list_based_on_board_design(
                    board_width_in_squares, board_height_in_squares, squareY, squareX
                )
            )
            print(position_in_list, " ", end="")
            print(
                PrintGameWrapper.players_token_is_in_position(
                    position_in_list, game.get_player_list()
                ),
                end="",
            )
            print("   |", end="")
        print()

    @staticmethod
    def get_position_in_list_based_on_board_design(
        board_width_in_squares: int,
        board_height_in_squares: int,
        squareY: int,
        squareX: int,
    ):
        list_size = board_width_in_squares * board_height_in_squares

        if squareY % 2 == 0:
            position_in_list = (
                (list_size + 1)
                - (
                    (squareY - 1) * board_width_in_squares
                    + ((board_width_in_squares) - squareX)
                )
                - 1
            )
        else:
            position_in_list = (list_size + 1) - (
                (squareY - 1) * board_width_in_squares + squareX
            )
        return position_in_list
