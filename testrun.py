#Alexander Mejia 
#QCC ID:24588520

import unittest
from main import Die, DiceGame

class TestDiceGame(unittest.TestCase):
    def test_die_roll_bounds(self):
        die = Die()
        for _ in range(100):
            roll = die.roll()
            self.assertTrue(1 <= roll <= 6)

    def test_evaluate_roll_win(self):
        game = DiceGame()
        self.assertEqual(game.evaluate_roll(7), "Win")
        self.assertEqual(game.evaluate_roll(11), "Win")
    def test_evaluate_roll_lose(self):
        game = DiceGame()
        for val in [2, 3, 12]:
            self.assertEqual(game.evaluate_roll(val), "Lose")        
    def test_play_round_result_structure(self):
        game = DiceGame()
        result = game.play_round()
        self.assertIn("die1", result)
        self.assertIn("die2", result)
        self.assertIn("total", result)
        self.assertIn("result", result)

        def test_evaluate_roll_roll_again(self):
            game = DiceGame()
            for val in [4, 5, 6, 8, 9, 10]:
                self.assertEqual(game.evaluate_roll(val), "Roll Again")   
    def test_different_die_sides(self):
        die = Die(sides=10)
        for _ in range(100):
            roll = die.roll()
            self.assertTrue(1 <= roll <= 10)
    def test_multiple_rounds(self):
        game = DiceGame()
        round1 = game.play_round()
        round2 = game.play_round()
        self.assertNotEqual(round1["total"], None)
        self.assertNotEqual(round2["total"], None)                             