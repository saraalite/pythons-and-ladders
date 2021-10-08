import pytest
from SnakesAndLadders.BoardGame.BoardGame import BoardGame


@pytest.fixture
def board_game():
    return BoardGame()


def test_last_answer_init_a(board_game):
    assert board_game.dummy_prop == 1


def test_last_answer_init(board_game):
    assert board_game.dummy_prop == 2
