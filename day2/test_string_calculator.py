from string_calculator import add
import unittest
import random

class TestAddStringCalculator(unittest.TestCase):

    def test_is_empty_zero(self):
        self.assertEqual(add(''), 0)
    def test_is_single_digit_same(self):
        self.assertEqual(add('1'), 1)
    def test_is_one_two_three(self):
        self.assertEqual(add('1,2'), 3)
    def test_add_supports_unknown_number_of_numbers(self):
        number_of_numbers = random.randint(1, 100)
        numbers = []
        for i in range(number_of_numbers):
            new_number = random.randint(0, 100)
            numbers.append(new_number)
        numbers_sum = sum(numbers)
        numbers_string = ', '.join(map(str, numbers))
        self.assertEqual(add(numbers_string), numbers_sum)
    def test_add_supports_newline_delimiter(self):
        self.assertEqual(add('1\n2,3'), 6)
    def test_add_supports_delimiter_declaration(self):
        self.assertEqual(add('//;\n1;2'), 3)
    def test_add_negative_number_throws_exception(self):
        self.assertRaises(Exception, add, '1,-2,3')

if __name__=='__main__':
    unittest.main()
