import unittest
import random

from string_calculator import add

class TestStringCalculator(unittest.TestCase):
    def test_add_empty_string_returns_zero(self):
        self.assertEqual(0, add(''))
    def test_add_single_number_string_returns_same_number_int(self):
        self.assertEqual(1, add('1'))
    def test_add_two_number_string_comma_delimited_returns_sum_int(self):
        self.assertEqual(3, add('1,2'))
    def test_add_unknown_number_of_numbers_returns_sum_int(self):
        number_of_numbers = random.randint(1, 100)
        numbers = [random.randint(0, 100) for i in range(number_of_numbers)]
        self.assertEqual(sum(numbers), add(','.join(map(str, numbers))))
    def test_add_newline_delimiter_in_string_returns_sum_int(self):
        self.assertEqual(6, add('1,2\n3'))
    def test_add_delimiter_declaration_in_string_returns_sum_int(self):
        self.assertEqual(3, add('//;\n1;2'))
    def test_add_negative_number_in_string_raises_exception(self):
        self.assertRaises(Exception, add, '1,-2,3')
