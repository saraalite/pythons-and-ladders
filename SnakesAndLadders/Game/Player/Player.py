class Player:
    def __init__(self):
        self.last_dice_result: int = None
        self.last_turn_played: int = 0
        self.is_winner: bool = False
        self.player_token_position: int = 1

    def get_last_dice_result(self) -> int:
        return self.last_dice_result

    def get_last_turn_played(self) -> int:
        return self.last_turn_played

    def get_is_winner(self) -> bool:
        return self.is_winner

    def get_player_token_position(self) -> int:
        return self.player_token_position

    def update_last_dice_result(self, dice_result):
        self.last_dice_result = dice_result

    def update_last_turn_played(self, turn_played):
        self.last_turn_played = turn_played

    def update_is_winner(self, is_winner):
        self.is_winner = is_winner

    def update_player_token_position(self, new_token_position):
        self.player_token_position = new_token_position
        self.update_last_turn_played(self.get_last_turn_played() + 1)
