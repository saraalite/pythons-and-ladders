from .Player.Player import Player
from .Board.Board import Board
from .Dice.Dice import Dice


class Game:
    def __init__(self, num_of_players):
        self.board: Board = Board()
        self.player_list = []
        for i in range(0, num_of_players):
            self.player_list.append(Player(position_in_player_list=i))

    def roll_dice_and_move_next_player(self):
        self.move_next_player(dice_result=Dice.roll())

    def move_next_player(self, dice_result):
        pass

    def get_board(self) -> Board:
        return self.board

    def get_player_list(self) -> "list[Player]":
        return self.player_list

    def is_there_a_winner(self) -> bool:
        return False
