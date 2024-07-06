import re

class Pattern:

    def __init__(self) -> None:
        self.connect_player_pattern = re.compile(r'ClientUserinfoChanged: \d n\\(.*?)\\')
        
        self.player_name_pattern = re.compile(r'(?<=n\\)(.*)(?=\\)')

        self.current_player = None

        self.killer_pattern = re.compile(r':\s([^:]+)\skilled\s(.*?)\sby\s[a-zA-Z_]+')

        self.world_kill_pattern = re.compile(r'killed (.+?) by')

        self.mean_death_pattern = re.compile(r'by (.+)$')

    
    def get_name(self):
       return self.current_player 
    

    def is_player_connected(self, line):
        match = self.connect_player_pattern.search(line)
        
        if match:
            self.current_player = match.group(1)
            return match
        
        return None
        
    def get_killer(self, line):
        match = self.killer_pattern.search(line)

        if match:
            return match.group(1)
        
    def get_killed_by_world(self, line):
        match = self.world_kill_pattern.search(line)
        if match:
            return match.group(1)
    
    def get_mean_death(self, line):
        match = self.mean_death_pattern.search(line)
        if match:
            return match.group(1)


