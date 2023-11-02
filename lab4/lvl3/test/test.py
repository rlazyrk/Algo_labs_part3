import unittest

from lab4.lvl3.src.lab4 import find_min_knight_path
from lab4.lvl3.src.lab4 import read_from_file


class TestMinKnightPath(unittest.TestCase):

    def test_required(self):
        board_sie, start, end = read_from_file("test_case_1.txt")
        self.assertEqual(find_min_knight_path(board_sie, start, end), 6)

    def test_small_board_one_move(self):
        board_size, start, end = read_from_file("test_case_2.txt")
        self.assertEqual(find_min_knight_path(board_size, start, end), 1)

    def test_small_board_many_move(self):
        board_size, start, end = read_from_file("test_case_3.txt")
        self.assertEqual(find_min_knight_path(board_size, start, end), 4)

    def text_from_corner_to_corner(self):
        self.assertEqual(find_min_knight_path(10, (9, 0), (0, 9)), 8)
