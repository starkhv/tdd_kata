import unittest
import random
from string_calculator import add

class TestStringCalculator(unittest.TestCase):

    def test_add_empty_string_returns_zero_int(self):
        self.assertEqual(0, add(''))
    def test_add_single_number_string_returns_same_number_int(self):
        self.assertEqual(1, add('1'))
    def test_add_two_numbers_comma_delimited_string_returns_sum_number_int(self):
        self.assertEqual(3, add('1,2'))
    def test_add_unknown_number_of_numbers_comma_delimited_string_returns_sum_number_int(self):
        number_of_numbers = random.randint(1, 100)
        numbers = [random.randint(0, 100) for i in range(number_of_numbers)]
        numbers_string = ','.join(map(str, numbers))
        self.assertEqual(sum(numbers), add(numbers_string))
    def test_add_newline_delimiter_works_along_with_comma_returns_sum_number_int(self):
        self.assertEqual(6, add('1,2\n3'))
    def test_add_delimiter_declaration_works_returns_sum_number_int(self):
        self.assertEqual(3, add('//;\n1;2'))
    def test_add_negative_number_in_delimited_string_raises_exception(self):
        # self.assertEqual(6, add('1,-2,3'))
        self.assertRaises(Exception, add, '1,-2,3')
