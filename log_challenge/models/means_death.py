class MeanDeath:
    game_index = 0
    def __init__(self) -> None:
        self.kill_by_means = {}
        MeanDeath.game_index += 1
        self.index = MeanDeath.game_index

    def count_mean(self, mean):
        if mean not in self.kill_by_means:
            self.kill_by_means[mean] = 1
        else:
            self.kill_by_means[mean] += 1

    def get_means_death(self):
        return {f'game-{self.index}':{'kills_by_means': self.kill_by_means}}
