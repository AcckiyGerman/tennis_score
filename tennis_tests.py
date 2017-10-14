import unittest
from tennis import Game


class TestTennisGame(unittest.TestCase):
    def testScoresList(self):
        self.assertEqual(Game.SCORES, ['love', 'fifteen', 'thirty', 'advantage', 'deuce'])

    def testStatus(self):
        game = Game()
        table = {(0, 0): 'love all',
                 (1, 0): 'fifteen love',
                 (2, 0): 'thirty love',
                 (3, 0): 'advantage player 1',
                 (4, 0): 'win player 1'}
        for scores, status in table.items():
            self.assertEqual(game.status(scores[0], scores[1]), status)


if __name__ == "__main__":
    unittest.main()
