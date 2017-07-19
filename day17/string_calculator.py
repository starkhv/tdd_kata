#!/usr/bin/env python3

""" Calculator that works on strings """

# built-in modules
import re

def add(numbers_string):
    # if string is not empty
    if len(numbers_string)>0:
        # regex for parsing delimiter declaration
        dd_regex = re.compile('//(?P<delimiter>.*)\n(?P<numbers_string>.*)')
        # parse numbers_string for delimiter declaration pattern
        dd_match = re.match(dd_regex, numbers_string)
        if dd_match:
            # make a dict from the parsed object
            dd_groups_dict = dd_match.groupdict()
            # list of delimiters contains the parsed delimiter
            delimiters = [dd_groups_dict['delimiter']]
            # update numbers_string to the parsed one
            numbers_string = dd_groups_dict['numbers_string']
        else:
            # default list of delimiters
            delimiters = ['\n', ',']
        # compile the delimiters regex
        delimiters_regex = re.compile(r'|'.join(map(re.escape, delimiters)))

        def neg_except_or_sum(numbers_string, delimiters_regex):
            """Raise exception with list of negative numbers if they are present
            Otherwise return sum of all numbers
            """
            # list of numbers in string
            numbers = list(map(int, re.split(delimiters_regex, numbers_string)))
            # filter list of negative numbers
            neg_numbers = list(filter(lambda x : x<0, numbers))
            # if negative numbers are present
            if len(neg_numbers)>0:
                raise(Exception('negatives not allowed ['+','.join(map(str, neg_numbers))))
            else:
                return sum(numbers)

        # split into numbers and return sum
        return neg_except_or_sum(numbers_string, delimiters_regex)
    # if string is empty
    else:
        return 0
