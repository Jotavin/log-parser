import re

def name(player_name) -> str:
    regex = r"(?<=n\\)(.*)(?=\\)"
    match = re.search(regex, player_name)
    return match.group(1)

def find_player(data) -> str:
    info = data
    player_name = name(info)
    return player_name

path = r'C:\Users\n7499\projects\log-challenge\log_challenge\scrape_data\quake_info.log'
with open(path, 'r') as file:
    logs_file = file.readlines()

start_index = None
end_index = None

jogos = []
jogadores = []

connect_player_pattern = re.compile(r'ClientUserinfoChanged: \d n\\(.*?)\\')
killer_pattern = re.compile(r':\s([^:]+)\skilled\s(.*?)\sby\s[a-zA-Z_]+')
# killer = re.compile(r'(?<=:\s)(.*?)(?=\skilled)')
# kill_player_pattern = re.compile(r': ([\w\s]+) killed')
# kill_player_pattern = re.compile(r'(\S+? killed \S+)|((<world>|\w+( \w+)*) killed (\w+( \w+)*))')
world_killer_pattern = re.compile(r'killed (.+?) by')


total_kills = []
for index, line in enumerate(logs_file):
    if 'InitGame' in line:
        print('achei')
        start_index = index
    
    if '---------' in line and start_index is not None:
        end_index = index
        match_kills = 0
        players = {}

        for i in range(start_index+1, end_index):
            
            match_connection = connect_player_pattern.search(logs_file[i])
            if match_connection:
                player = find_player(match_connection.group())
                if player not in players:
                    players[player] = 0

            if 'Kill:' in logs_file[i]:
                match_kills += 1
                killer = killer_pattern.search(logs_file[i]).group(1)
                worlds_kill = world_killer_pattern.search(logs_file[i]).group(1)

                print(killer)
                print(players)
                if '<world>' == killer:
                    players[worlds_kill] -= 1

                else:
                    players[killer] += 1






        total_kills.append(match_kills)
        jogadores.append(players)

        start_index = None

print(jogadores)
print(total_kills)
print(players)






