import random

class Game:
    SCORES = ['love', 'fifteen', 'thirty', 'advantage', 'deuce']

    def __init__(self):
        self.player1score = 0
        self.player2score = 0

    def game_score(self):
        pass

    def name_score(self, n):
        return self.SCORES[n]



