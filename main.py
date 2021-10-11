from SnakesAndLadders.Game.Game import Game


def print_game_status(game: Game):
    for index, player in enumerate(game.get_player_list()):
        print("Player num: ", index)
        print("Last turn played: ", player.get_last_turn_played())
        print("Last dice result: ", player.get_last_dice_result())
        print("Player token position: ", player.get_player_token_position())
        print("--------------------------------------------------------")


def print_welcome():
    print(
        "===========================WELCOME TO PYTHONS AND LADDERS==========================="
    )


def get_number_of_players():
    print("Enter number of players: ")
    number_of_players = int(input())
    return number_of_players


game = Game(num_of_players=get_number_of_players())

print_welcome()

while not (game.is_there_a_winner()):
    print("Press enter to roll the dice for next player")
    input()
    game.roll_dice_and_move_next_player()
    print_game_status(game)

if game.is_there_a_winner():
    print("We have a winner")
    print("Congrats to player ", game.get_winner_player_number())
