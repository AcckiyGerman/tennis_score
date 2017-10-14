import random


class Game:
    SCORES = ['love', 'fifteen', 'thirty', 'advantage', 'deuce']

    def __init__(self):
        self.player1score = 0
        self.player2score = 0

    def status(self, p1, p2):
        """:returns status of the game depending of both players scores"""
        if p1 > 3 and p1 > p2 + 1:
            return 'win player 1'
        elif p1 > 2 and p1 > p2:
            return 'advantage player 1'
        elif p1 == p2:
            if p1 < 3:
                return self.SCORES[p1] + ' all'
            else:
                return 'deuce'
        else:
            return "{0} {1}".format(self.SCORES[p1], self.SCORES[p2])


