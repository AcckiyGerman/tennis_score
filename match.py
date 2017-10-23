from set import TennisSet


class Match:
    """
    Representing the Tennis Match.
    Match consists of maximum three tennis sets.
    The player wins the match, when he won two sets.
    """
    def __init__(self):
        self.player1score = 0
        self.player2score = 0
        self.sets = []

    def play(self):
        print('#'*10, 'The Tennis Match is started.')
        pass

    def print_results(self):
        pass


if __name__ == '__main__':
    match = Match()
    match.play()
