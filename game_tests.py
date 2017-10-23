import unittest
from game import Game


class TestTennisGame(unittest.TestCase):
    def testScoresList(self):
        self.assertEqual(Game.SCORES, ['love', 'fifteen', 'thirty'])

    def testStatus(self):
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
            game = Game()
            game.player1score = scores[0]
            game.player2score = scores[1]

            self.assertEqual(game.status(), status)

    def testPlayPitch(self):
        game = Game()
        for i in range(10):
            p1 = game.player1score
            p2 = game.player2score
            game.play_a_pitch()
            self.assertTrue(game.player1score == p1 + 1 or game.player2score == p2 + 1)

    def testPlayGame(self):
        for i in range(10):
            game = Game()
            result = game.play()
            self.assertIn(result, ['win player 1', 'win player 2'])

if __name__ == "__main__":
    unittest.main()
