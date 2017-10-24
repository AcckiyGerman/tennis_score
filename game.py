from random import random


class GameError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Game:
    SCORES = ['love', 'fifteen', 'thirty']

    def __init__(self):
        self.player1score = 0
        self.player2score = 0

    def status(self):
        """:returns status of the game depending of both players scores"""
        p1 = self.player1score
        p2 = self.player2score

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
        if 'win' in self.status():
            raise GameError('This game is over, start a new game please.')

        print('\n\tThe tennis game is started.')
        print(self.status())

        while True:
            self.play_a_pitch()
            status = self.status()
            print(status)
            if 'win' in status:
                return status


if __name__ == '__main__':
    game = Game()
    game.play()
