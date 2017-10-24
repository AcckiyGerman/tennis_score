import unittest
from set import TennisSet


class TestTennisSet(unittest.TestCase):
    def testSetStatus(self):
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
            self.assertEqual(result, s.status())

    def testSetPlay(self):
        for i in range(10):
            s = TennisSet()
            result = s.play()
            self.assertIn(result, ['player 1 win the set', 'player 2 win the set'])
            # check the score count is correct
            p1 = s.player1score
            p2 = s.player2score
            self.assertTrue(p1 >= 6 or p2 >= 6)
            self.assertTrue(abs(p1 - p2) > 1)

if __name__ == "__main__":
    unittest.main()
