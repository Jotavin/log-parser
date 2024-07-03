class Game:

    def __init__(self) -> None:
        self.total_kills = 0
        self.players = []
        self.kills = {}

    def __str__(self) -> str:
        return f'{self.game}'
    
    def add_players(self, players):
        self.players = [players[player] for player in players]


    def set_total_kills(self, total_kills):
        self.total_kills = total_kills

    def get_players_match(self):
        return {player.name:player.kills for player in self.players}

    def get_players_name(self):
        return [player.name for player in self.players]

    def get_game_info(self):
        return {'total_kills':self.total_kills, 'players': self.get_players_name(), 'kills': self.get_players_match()}

    # def get_game_info(self):
    #     return {game.player: game.player_kills for game in self.player}