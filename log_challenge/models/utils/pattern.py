import re

class Pattern:

    def __init__(self) -> None:
        self.connect_player_pattern = re.compile(r'ClientUserinfoChanged: \d n\\(.*?)\\')
        
        self.player_name_pattern = re.compile(r'(?<=n\\)(.*)(?=\\)')

        self.current_player = None

        self.killer_pattern = re.compile(r':\s([^:]+)\skilled\s(.*?)\sby\s[a-zA-Z_]+')

        self.killed_pattern = re.compile

        

    
    def get_name(self):
       return self.current_player 
        # match = self.player_name_pattern.search(self.current_player)
        # if match:
        #     return match.group(1)
        # return None

    def is_player_connected(self, line):
        match = self.connect_player_pattern.search(line)


        if match:
            self.current_player = match.group(1)
            return match
        
        return None
        


