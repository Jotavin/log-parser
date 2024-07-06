from models.player import Player
from models.game import Game
from models.means_death import MeanDeath
from models.utils.pattern import Pattern



def parser_quake():
    path = r'qgames.log'
    with open(path, 'r') as file:
        logs_file = file.readlines()

    start_index = None
    end_index = None

    games = []
    means_death = []

    p = Pattern()
    for index, line in enumerate(logs_file):
        if 'InitGame' in line:

            start_index = index
        
        if '---------' in line and start_index is not None:
            end_index = index
            match_kills = 0
            players = {}

            current_means_death = MeanDeath()
            for line in range(start_index+1, end_index):
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
                    
                    mean = p.get_mean_death(logs_file[line])

                    current_means_death.count_mean(mean)


            start_index = None
            
            current_game = Game()
            current_game.set_total_kills(match_kills)
            current_game.add_players(players)

            games.append(current_game)

            
            means_death.append(current_means_death)

    return games, means_death


if __name__ == '__main__':
    games, md = parser_quake()

    for game in games:
        print(game.get_game_info())

    for item in md:
        print(item.get_means_death())