import re
from src.player import Player
from src.game import Game


def name(player_name) -> str:
    regex = r'(?<=n\\)(.*)(?=\\)'
    match = re.search(regex, player_name)
    return match.group(1)

def find_player(data) -> str:
    info = data
    player_name = name(info)
    return player_name

path = r'qgames.log'
with open(path, 'r') as file:
    logs_file = file.readlines()

start_index = None
end_index = None

jogos = []


connect_player_pattern = re.compile(r'ClientUserinfoChanged: \d n\\(.*?)\\')
killer_pattern = re.compile(r':\s([^:]+)\skilled\s(.*?)\sby\s[a-zA-Z_]+')
# killer = re.compile(r'(?<=:\s)(.*?)(?=\skilled)')
# kill_player_pattern = re.compile(r': ([\w\s]+) killed')
# kill_player_pattern = re.compile(r'(\S+? killed \S+)|((<world>|\w+( \w+)*) killed (\w+( \w+)*))')
world_killer_pattern = re.compile(r'killed (.+?) by')

games = []

total_kills = []
for index, line in enumerate(logs_file):
    if 'InitGame' in line:

        start_index = index
    
    if '---------' in line and start_index is not None:
        end_index = index
        match_kills = 0
        players = {}

        for line in range(start_index+1, end_index):
            
            match_connection = connect_player_pattern.search(logs_file[line])
            if match_connection:
                player_name = find_player(match_connection.group())
                if player_name not in players:
                    players[player_name] = Player(player_name)

            if 'Kill:' in logs_file[line]:
                match_kills += 1
                killer = killer_pattern.search(logs_file[line]).group(1)
                worlds_kill = world_killer_pattern.search(logs_file[line]).group(1)


                if '<world>' == killer:
                    players[worlds_kill].subtract_kill()

                else:
                    players[killer].add_kill()

        start_index = None




        current_game = Game()
        current_game.set_total_kills(match_kills)
        current_game.add_players(players)

        games.append(current_game)

        total_kills.append(match_kills)




print(game.get_game_info())
print(games)
for game in games:
    print(game.get_game_info())





