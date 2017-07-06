import unittest
import random

from string_calculator import add

class TestStringCalculator(unittest.TestCase):

    def test_add_empty_string_returns_zero(self):
        self.assertEqual(0, add(''))
    def test_add_single_number_returns_same_number(self):
        self.assertEqual(1, add('1'))
    def test_add_two_numbers_returns_sum(self):
        self.assertEqual(3, add('1,2'))
    def test_add_unknown_number_of_numbers_returns_sum(self):
        number_of_numbers = random.randint(1, 100)
        numbers = [random.randint(1, 100) for i in range(number_of_numbers)]
        self.assertEqual(sum(numbers),add(','.join(map(str, numbers))))
    def test_add_works_with_newline_delimiter(self):
        self.assertEqual(3, add('1\n2'));
    def test_add_works_with_delimiter_declaration(self):
        self.assertEqual(3, add('//;\n1;2'))
    def test_add_negative_number_in_string_throws_exception(self):
        self.assertRaises(Exception, add, '1,-2,3')
