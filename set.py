from game import Game


class SetError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class TennisSet:
    """
    Representing the Tennis Set.
    Set consists of tennis games.
    One won game give a player one point.
    The player wins the set, when he won at least 6 games AND have two points advantage.
    """
    def __init__(self):
        self.player1score = 0
        self.player2score = 0

    def status(self):
        """ :return: status of the set depending of both players scores"""
        p1 = self.player1score
        p2 = self.player2score

        if p1 >= 6 and p1 > p2 + 1:
            return 'player 1 win the set'
        elif p2 >= 6 and p2 > p1 + 1:
            return 'player 2 win the set'
        else:
            s1 = p1 or 'love'  # in case when score = 0 we say 'love'
            s2 = p2 or 'love'
            return '{0} - {1}'.format(s1, s2)

    def play(self):
        """
        Starts the tennis set and loops over games, until the winner is defined.
        :return: status of the set
        """
        if 'win' in self.status():
            raise SetError('This set is over, start a new set please.')

        print('\n\t\t The set is started.')

        while True:
            game = Game()
            game_status = game.play()
            if game_status == 'win player 1':
                self.player1score += 1
            elif game_status == 'win player 2':
                self.player2score += 1

            set_status = self.status()
            print('\tSet status:', set_status)

            if 'win' in set_status:
                return set_status


if __name__ == '__main__':
    tennisSet = TennisSet()
    tennisSet.play()
