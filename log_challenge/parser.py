import re
from models.player import Player
from models.game import Game
from models.utils.pattern import Pattern

p = Pattern()

path = r'qgames.log'
path = r'C:\Users\n7499\projects\log-challenge\log_challenge\qgames.log'
with open(path, 'r') as file:
    logs_file = file.readlines()

start_index = None
end_index = None

games = []

for index, line in enumerate(logs_file):
    if 'InitGame' in line:

        start_index = index
    
    if '---------' in line and start_index is not None:
        end_index = index
        match_kills = 0
        players = {}

        for line in range(start_index+1, end_index):
            l = logs_file[line]
            if p.is_player_connected(logs_file[line]):

                player_name = p.get_name()
                if player_name not in players:
                    players[player_name] = Player(player_name)

            if 'Kill:' in logs_file[line]:
                match_kills += 1
                killer = p.get_killer(logs_file[line])


                if '<world>' == killer:
                    worlds_kill = p.get_killed_by_world(logs_file[line])
                    players[worlds_kill].subtract_kill()

                else:
                    players[killer].add_kill()

        start_index = None

        current_game = Game()
        current_game.set_total_kills(match_kills)
        current_game.add_players(players)

        games.append(current_game)








for game in games:
    print(game.get_game_info())





