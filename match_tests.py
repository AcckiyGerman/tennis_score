import unittest
from match import Match
from set import TennisSet


class MatchTest(unittest.TestCase):
    def testMatchPlay(self):
        for _ in range(10):
            m = Match()
            m.play()
            self.assertNotEqual(m.player1score, m.player2score)
            self.assertTrue(2 <= len(m.sets) <= 3)
            for tennis_set in m.sets:
                self.assertIsInstance(tennis_set, TennisSet)
            if len(m.sets) == 2:
                self.assertTrue(m.player1score == 0 or m.player2score == 0)

    def testMatchPrintResults(self):
        pass


if __name__ == "__main__":
    unittest.main()
