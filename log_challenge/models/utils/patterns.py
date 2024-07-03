import re

class Patterns:

    def __init__(self) -> None:
        self.connect_player_pattern = re.compile(r'ClientUserinfoChanged: \d n\\(.*?)\\')
        
        self.player_name_pattern = re.compile(r'(?<=n\\)(.*)(?=\\)')

        self.current_player = None

        self.killer_pattern = re.compile(r':\s([^:]+)\skilled\s(.*?)\sby\s[a-zA-Z_]+')

        

    
    def name(self):
        
        match = self.player_name_pattern.search(self.current_player_string)
        if match:
            return match.group(1)
        return None

    def is_player_connected(self, line):
        match = self.connect_player_pattern.search(line)


        if match:
            self.current_player = match
            return match
        
        return None
        


