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
        print('#'*10, 'The Tennis Match is started.', '#'*10)
        while self.player1score < 2 and self.player2score < 2:
            s = TennisSet()
            result = s.play()
            self.sets.append(s)
            if 'player 1 win' in result:
                self.player1score += 1
            elif 'player 2 win' in result:
                self.player2score += 1

        self.print_results()

    def print_results(self):
        pass


if __name__ == '__main__':
    match = Match()
    match.play()
