from .Dice.Dice import Dice
from .Player.Player import Player
from .Board.Board import Board


class Game:
    def __init__(self):
        self.board: Board = Board()
        self.player_list: list[Player] = [
            Player(position_in_player_list=0),
            Player(position_in_player_list=1),
        ]

    def roll_dice_and_move(self):
        print("Holi")

    def get_board(self):
        return self.board

    def get_player_list(self):
        return self.player_list

    def get_game_status(self):
        print("Holi")
