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
        """Starts the tennis match and loops over sets, until the winner is defined."""
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
        """Prints pretty formatted results of the Tennis match."""
        sets = " ".join('%d-%d' % (s.player1score, s.player2score) for s in self.sets)
        winner = 'Player 1' if self.player1score > self.player2score else 'Player 2'
        match_message = """
        ########## The Tennis Match is finished. ##########
                    Sets: {sets}
                    {winner} is the winner!
        ###################################################
        """.format(sets=sets, winner=winner)
        print(match_message)

if __name__ == '__main__':
    match = Match()
    match.play()
