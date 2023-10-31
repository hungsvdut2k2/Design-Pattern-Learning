from player import Player


class Team:
    def __init__(self, name: str) -> None:
        self.name = name
        self.players = []

    def add_player(self, player: Player):
        self.players.append(player)

    def get_player_info(self, number: int):
        chosen_player = [
            self.players[i]
            for i in range(len(self.players))
            if self.players[i].number == number
        ]
        return (
            f"{chosen_player[0].name} ({chosen_player[0].position}) - {chosen_player[0].number}"
            if len(chosen_player) != 0
            else "Player not found"
        )
