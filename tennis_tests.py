import unittest
from tennis import Game


class TestTennisGame(unittest.TestCase):
    def testScoresList(self):
        self.assertEqual(Game.SCORES, ['love', 'fifteen', 'thirty'])

    def testStatus(self):
        game = Game()
        table = {
                 # equal score
                 (0, 0): 'love all',
                 (1, 1): 'fifteen all',
                 (2, 2): 'thirty all',
                 (3, 3): 'deuce',
                 (5, 5): 'deuce',
                 (9, 9): 'deuce',
                 # p1 > p2
                 (1, 0): 'fifteen love',
                 (2, 0): 'thirty love',
                 (3, 0): 'advantage player 1',
                 (4, 0): 'win player 1',
                 # p2 > p1
                 (0, 1): 'love fifteen',
                 (0, 2): 'love thirty',
                 (0, 3): 'advantage player 2',
                 (0, 4): 'win player 2',
                 # close game, when scores < 3
                 (2, 1): 'thirty fifteen',
                 (1, 2): 'fifteen thirty',

                 # close game, when scores => 3
                 (3, 2): 'advantage player 1',
                 (2, 3): 'advantage player 2',
                 (5, 6): 'advantage player 2',
                 (7, 6): 'advantage player 1',
                 # win
                 (4, 2): 'win player 1',
                 (2, 4): 'win player 2',
                 (5, 3): 'win player 1',
                 (6, 8): 'win player 2'}

        for scores, status in table.items():
            self.assertEqual(game.status(scores[0], scores[1]), status)


if __name__ == "__main__":
    unittest.main()
