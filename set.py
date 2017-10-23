from game import Game


class Set:
    """
    Representing the Tennis Set.
    Set consists of tennis games.
    One won game give a player one point.
    The player wins the set, when he won at least 6 games AND have two points advantage.
    """
    def __init__(self):
        self.player1score = 0
        self.player2score = 0

    def score(self):
        """ :return: status of the set depending of both players scores"""
        pass

    def play(self):
        """
        Starts the tennis set and loops over games, until the winner is defined.
        :return: status of the set
        """
        pass
