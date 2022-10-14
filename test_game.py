'''Unittest of Rock Paper Scissors Game'''
# Student Name: Chen Chen
# Student Number: S360496
import unittest
from game import Game


class MyTestCase(unittest.TestCase):
    '''Use unittest to test the game.'''
    game = Game()

    def test_input(self):
        '''Test if input is valid.'''
        self.assertTrue(self.game.is_input_valid("paper"))
        self.assertTrue(self.game.is_input_valid("PAPER"))
        self.assertTrue(self.game.is_input_valid("Paper"))
        self.assertFalse(self.game.is_input_valid("0"))
        self.assertFalse(self.game.is_input_valid("p"))
        self.assertFalse(self.game.is_input_valid("$"))

    def get_result(self):
        '''Test if the winner is the correct one.'''
        self.assertEqual(self.game.get_result("paper", "scissors"), "computer")
        self.assertEqual(self.game.get_result("paper", "rock"), "user")
        self.assertEqual(self.game.get_result("paper", "paper"), "tie")
        self.assertEqual(self.game.get_result("rock", "scissors"), "user")
        self.assertEqual(self.game.get_result("rock", "rock"), "tie")
        self.assertEqual(self.game.get_result("rock", "paper"), "computer")
        self.assertEqual(self.game.get_result("scissors", "rock"), "computer")
        self.assertEqual(self.game.get_result("scissors", "scissors"), "tie")
        self.assertEqual(self.game.get_result("scissors", "paper"), "user")


if __name__ == '__main__':
    unittest.main()
