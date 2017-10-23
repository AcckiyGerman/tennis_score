import unittest
from set import TennisSet


class TestTennisSet(unittest.TestCase):
    def testSetScore(self):
        set_table = {
            (0, 0): 'love - love',
            (1, 0): '1 - love',
            (0, 1): 'love - 1',
            (1, 1): '1 - 1',
            (3, 4): '3 - 4',
            (5, 5): '5 - 5',
            (6, 5): '6 - 5',
            (5, 6): '5 - 6',

            (7, 5): 'player 1 win the set',
            (3, 6): 'player 2 win the set',
            (0, 6): 'player 2 win the set',
            (100, 98): 'player 1 win the set',

            (100000, 100001): '100000 - 100001'
        }
        for score, result in set_table.items():
            s = TennisSet()
            s.player1score = score[0]
            s.player2score = score[1]
            self.assertEqual(result, s.score())

    def testSetPlay(self):
        pass


if __name__ == "__main__":
    unittest.main()
