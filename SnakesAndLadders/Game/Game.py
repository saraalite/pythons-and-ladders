from .Player.Player import Player
from .Board.Board import Board
from .Dice.Dice import Dice


class Game:
    def __init__(self, num_of_players):
        self.board: Board = Board()
        self.player_list: list[Player] = []
        for i in range(0, num_of_players):
            self.player_list.append(Player())

    def roll_dice_and_move_next_player(self):
        self.move_next_player(dice_result=Dice.roll())

    def move_next_player(self, dice_result):
        if not (self.is_there_a_winner()):
            next_player = self.get_next_player()
            next_position = self.board.get_next_position_based_on_dice_result(
                current_position=next_player.get_player_token_position(),
                dice_result=dice_result,
            )

            next_player.update_player_token_position(next_position)
            next_player.update_last_dice_result(dice_result)

            if next_position == self.board.get_last_position_in_board():
                next_player.update_is_winner(True)

    def get_board(self) -> Board:
        return self.board

    def get_player_list(self) -> "list[Player]":
        return self.player_list

    def is_there_a_winner(self) -> bool:
        return self.get_winner_player_number() != None

    def get_winner_player_number(self) -> int:
        winner_player_number = None
        for index, player in enumerate(self.player_list):
            if player.get_is_winner():
                winner_player_number = index

        return winner_player_number

    def get_next_player(self) -> Player:
        last_turn_played = self.get_last_turn_played_in_game()
        next_player = None

        for player in self.player_list:
            if next_player == None and player.get_last_turn_played() < last_turn_played:
                next_player = player

        if next_player == None:
            next_player = self.player_list[0]

        return next_player

    def get_last_turn_played_in_game(self) -> int:
        last_turn_played = 0
        for player in self.player_list:
            if player.get_last_turn_played() > last_turn_played:
                last_turn_played = player.get_last_turn_played()

        return last_turn_played
