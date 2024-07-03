class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.kills = 0

    
    def set_kills(self, kills_value) -> None:
        self.kills = kills_value

    def add_kill(self):
        self.kills += 1

    def subtract_kill(self):
        self.kills -= 1

    def __str__(self) -> str:
        return f'{self.name}: {self.kills}'
    
    