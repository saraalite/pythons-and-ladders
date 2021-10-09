import pytest
from SnakesAndLadders.Game.Game import Game
from SnakesAndLadders.Game.Dice.Dice import Dice
from SnakesAndLadders.Game.Dice.DiceValues.DiceValues import DiceValues


@pytest.fixture
def game() -> Game:
    return Game(num_of_players=1)


def test_us_1_token_can_move_across_the_board(game: Game):
    game.move_next_player(dice_result=3)
    player = game.get_player_list()[0]

    assert player.get_player_token_position() != 1


def test_us_1_uat_1_at_the_beginning_the_tokens_are_in_position_one(game: Game):
    player = game.get_player_list()[0]

    assert player.get_player_token_position() == 1


def test_us_1_uat_2_token_from_position_1_to_4(game: Game):
    game.move_next_player(dice_result=3)
    player = game.get_player_list()[0]

    assert player.get_player_token_position() == 4


def test_us_1_uat_3_token_from_position_4_to_8(game: Game):
    game.move_next_player(dice_result=3)
    game.move_next_player(dice_result=4)
    player = game.get_player_list()[0]

    assert player.get_player_token_position() == 8


def test_us_2_uat_1_token_from_position_97_to_100(game: Game):
    player = game.get_player_list()[0]
    player.update_player_token_position(97)
    game.move_next_player(dice_result=3)

    assert player.get_player_token_position() == 100 and player.get_is_winner()


def test_us_2_uat_2_token_position_97_and_get_4_with_dice(game: Game):
    player = game.get_player_list()[0]
    player.update_player_token_position(97)
    game.move_next_player(dice_result=4)

    assert player.get_player_token_position() == 97 and player.get_is_winner() == False


def test_us_3_uat_1_dice_result_between_1_and_6(game: Game):
    dice_result = Dice.roll()

    assert Dice.roll() >= 1 and dice_result <= 6


def test_us_3_uat_2_dice_rolls_4_and_token_moves_4_spaces(game: Game):
    player = game.get_player_list()[0]
    initial_position = player.get_player_token_position()
    game.move_next_player(dice_result=DiceValues.FOUR)

    assert player.get_player_token_position() == initial_position + 4
