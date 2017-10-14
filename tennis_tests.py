import unittest
from tennis import Game


class TestTennisGame(unittest.TestCase):
    def testScoresList(self):
        self.assertEqual(Game.SCORES, ['love', 'fifteen', 'thirty', 'advantage', 'deuce'])


if __name__ == "__main__":
    unittest.main()
