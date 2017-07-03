import unittest
from string_calculator import add
import random
import pdb

class TestStringCalculator(unittest.TestCase):

    def test_is_add_empty_zero(self):
        self.assertEqual(add(''), 0)

    def test_is_add_one_one(self):
        self.assertEqual(add('1'), 1)

    def test_is_add_one_two_three(self):
        self.assertEqual(add('1, 2'), 3)

    def test_add_handles_unknown_number_of_numbers(self):
        random_number = random.randint(0, 100)
        number_string = ''
        actual_sum = 0
        for i in range(random_number):
            random_number2 = random.randint(0, 100)
            if not i == 0:
                number_string += ', '
            number_string += str(random_number2)
            actual_sum += random_number2
        self.assertEqual(add(number_string), actual_sum)

    def test_add_handles_newlines(self):
        self.assertEqual(add('1\n2,3'), 6)

    def test_add_handles_delimiter_declaration(self):
        self.assertEqual(add('//;\n1;2'), 3)

    def test_negative_number_raises_exception(self):
        self.assertRaises(Exception, add, '-1,2,3')

    def test_number_bigger_than_1000_ignored(self):
        self.assertEqual(add('1,2,3,4,1001'), 10)

    def test_add_handles_delimiters_of_any_length_declaration(self): 
        self.assertEqual(add('//[***]\n1***2***3'), 6)

    def test_add_handles_multiple_delimiters_declaration(self): 
        self.assertEqual(add('//[*][d]\n1*2d3'), 6)

    def test_add_handles_multiple_delimiters_of_any_length_declaration(self): 
        self.assertEqual(add('//[***][dd]\n1***2dd3'), 6)

if __name__ == '__main__':
    unittest.main()
