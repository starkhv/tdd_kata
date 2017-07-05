import unittest
import random

from string_calculator import add

class TestStringCalculator(unittest.TestCase):

    def test_add_emptyString_returns0(self):
        self.assertEqual(0, add(''))
    def test_add_singleNumberString_returnsNumber(self):
        self.assertEqual(1, add('1'))
    def test_add_twoNumbersString_returnSum(self):
        self.assertEqual(3, add('1,2'))
    def test_add_unknownNumberOfNumbersString_returnSum(self):
        number_of_numbers = random.randint(1,100)
        numbers = []
        for i in range(number_of_numbers):
            new_number = random.randint(1,100)
            numbers.append(new_number)
        numbers_sum = sum(numbers)
        numbers_string = ','.join(map(str, numbers))
        self.assertEqual(numbers_sum, add(numbers_string))
    def test_add_newlineDelimiter_works(self):
        self.assertEqual(6, add('1,2\n3'))
    def test_add_delimiterDeclaration_works(self):
        self.assertEqual(3, add('//;\n1;2'))
    def test_add_negativeNumberPresent_raisesException(self):
        self.assertRaises(Exception, add, '1,-2,3')
