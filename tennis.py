from random import random


class Game:
    SCORES = ['love', 'fifteen', 'thirty']

    def __init__(self):
        self.player1score = 0
        self.player2score = 0

    def status(self, p1, p2):
        """:returns status of the game depending of both players scores"""
        if p1 > 3 and p1 > p2 + 1:
            return 'win player 1'
        elif p2 > 3 and p2 > p1 + 1:
            return 'win player 2'
        elif p1 > 2 and p1 > p2:
            return 'advantage player 1'
        elif p2 > 2 and p2 > p1:
            return 'advantage player 2'
        elif p1 == p2:
            if p1 < 3:
                return self.SCORES[p1] + ' all'
            else:
                return 'deuce'
        else:
            return "{0} {1}".format(self.SCORES[p1], self.SCORES[p2])

    def play_a_pitch(self):
        if random() < 0.5:
            self.player1score += 1
        else:
            self.player2score += 1

    def play(self):
        print('The tennis game is started. Score:')
        print(self.status(self.player1score, self.player2score))

        while True:
            self.play_a_pitch()
            status = self.status(self.player1score, self.player2score)
            print(status)
            if 'win' in status:
                break


if __name__ == '__main__':
    game = Game()
    game.play()
