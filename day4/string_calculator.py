import re

def add(numbers_string):
    if len(numbers_string)>0:
        # delimiter declaration regex pattern
        dd_pattern = r'//(?P<delimiter>.*)\n(?P<numbers_string>.*)'
        # check if delimiter is declared
        dd_match = re.match(dd_pattern, numbers_string)
        if dd_match:
            # delmiter declaration group dictionary
            dd_dict = dd_match.groupdict()
            delimiters = [dd_dict['delimiter']]
            numbers_string = dd_dict['numbers_string']
        else:
            # list of delimiters
            delimiters = [',', '\n']
        # delimiter regex of splitting for regex based splitting
        delimiters_regex = '|'.join(map(re.escape, delimiters))
        def neg_except(numbers):
            """Raise exception when a number in numbers in negative"""
            numbers = list(numbers)
            neg_numbers = list(filter(lambda x: x<0, numbers))
            if len(neg_numbers)>0:
                raise(Exception('negatives not allowed ['+','.join(neg_numbers)+']'))
            return numbers
        # list of numbers in the given string
        numbers = map(int, re.split(delimiters_regex, numbers_string))
        # check none of the numbers is negative
        numbers = neg_except(numbers)
        return sum(numbers)
    else:
        return 0
