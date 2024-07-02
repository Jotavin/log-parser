import re

def name(player_name):
    regex = r"(?<=n\\)(.*)(?=\\)"
    match = re.search(regex, player_name)
    return match.group(1)

def find_player(data):
    info = data
    player_name = name(info)
    return player_name

path = r'C:\Users\n7499\projects\log-challenge\log_challenge\qgames.log'
with open(path, 'r') as file:
    logs_file = file.readlines()

start_index = None
end_index = None

jogos = []
jogadores = []
# encontrar player
pattern = re.compile(r'ClientUserinfoChanged: \d n\\(.*?)\\')
# encontrar mortes
# condições -> achar Kill na string > se <world> conter na string -1 kill pro killed
#                                     se diferente de <world> +1 kill pro killer
total_kills = []
for index, line in enumerate(logs_file):
    if 'InitGame' in line:
        print('achei')
        start_index = index
    
    if '---------' in line and start_index is not None:
        end_index = index
        match_kills = 0
        players = []
        #percorrer do start+1 até o end > buscando players > kills
        for i in range(start_index+1, end_index):
            if 'Kill:' in logs_file[i]:
                match_kills += 1
            match = pattern.search(logs_file[i])
            if match:
                player = find_player(match.group())
                if player not in players:
                    players.append(player)
        total_kills.append(match_kills)
        jogadores.append(players)

        start_index = None

print(jogadores)
print(total_kills)






