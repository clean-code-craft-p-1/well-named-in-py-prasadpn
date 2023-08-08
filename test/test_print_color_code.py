from print_color_code import print_wire_color_code
import unittest


class test_print_output(unittest.TestCase):

    def test_print_output_with_header(self, pair_number):
        expected = '\n'.join(['|   Pair Number | Major   | Minor   |',
                              '|---------------+---------+---------|',
                              '|            25 | Violet  | Slate   |'])
        result = print_wire_color_code(pair_number)
        self.assertEqual(expected, result)
