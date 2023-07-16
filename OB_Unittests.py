import unittest
from OrthokonBoard import OrthokonBoard

class TestOrthokonBoard(unittest.TestCase):

    def test_valid_move_vertical(self):
        game = OrthokonBoard()
        is_valid = game.make_move(3,0,1,0)
        self.assertTrue(is_valid)

    def test_valid_move_horizontal(self):
        game = OrthokonBoard()
        game.make_move(0,1,2,1)  # move red piece off starting line
        is_valid = game.make_move(2,1,2,3)
        self.assertTrue(is_valid)

    def test_valid_move_diagonal(self):
        game = OrthokonBoard()
        is_valid = game.make_move(0,0,2,2)
        self.assertTrue(is_valid)
    
    def test_out_of_bounds(self):
        game = OrthokonBoard()
        out_of_bounds = game.make_move(3,0,-1,2)
        self.assertFalse(out_of_bounds)

    def test_move_0_spaces(self):
        game = OrthokonBoard()
        move_0_spaces = game.make_move(3,2,3,2)
        self.assertFalse(move_0_spaces)

    def test_move_not_max_dist(self):
        game = OrthokonBoard()
        move_not_max = game.make_move(3,0,2,0)
        self.assertFalse(move_not_max)

    def test_move_to_occupied_space(self):
        game = OrthokonBoard()
        space_occupied = game.make_move(3,0,0,0)
        self.assertFalse(space_occupied)

    def test_move_empty_space(self):
        game = OrthokonBoard()
        move_empty = game.make_move(2,0,2,3)
        self.assertFalse(move_empty)

    def test_yellow_wins(self):
        game = OrthokonBoard()
        game.make_move(3,0,1,0)
        game.make_move(3,1,1,1)
        game.make_move(3,2,1,2)
        game.make_move(3,3,1,3)
        status = game.get_current_state()
        self.assertEqual(status, "YELLOW_WINS")

    def test_red_wins(self):
        game = OrthokonBoard()
        game.make_move(0,0,2,0)
        game.make_move(0,1,2,1)
        game.make_move(0,2,2,2)
        game.make_move(0,3,2,3)
        status = game.get_current_state()
        self.assertEqual(status, "RED_WINS")


if __name__ == '__main__':
    unittest.main()
