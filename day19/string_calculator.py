#!/usr/bin/env python3

""" Calculator that takes in a string and does computations based on the contents of the string """

# built-in modules
import re


# NOTE: compile all regexes for speed


def add(numbers_string):
    """ Add the numbers in the input string based on the contents """
    # if given string is empty
    if len(numbers_string)==0:
        return 0
    else:
        # regex to match delimiter declaration
        dd_regex = re.compile(r'//(?P<delimiter>.*)\n(?P<numbers_string>.*)')
        # match delimiter declaration with input string
        dd_match = re.match(dd_regex, numbers_string)
        # if there is a delimiter declaration then parse
        if dd_match:
            # parse the groups in the regex to a dict
            dd_groups = dd_match.groupdict()
            # list of delimiters with the parsed delimiter
            delimiters = [dd_groups['delimiter']]
            # overwrite numbers_string with parsed numbers_string
            numbers_string = dd_groups['numbers_string']
        else:
            # list of delimiters
            delimiters = [',', '\n']
        # regex to match delimiters
        delimiters_regex = re.compile(r'|'.join(map(re.escape, delimiters)))

        def neg_except_or_sum(delimiters_regex, numbers_string):
            """ Raise exception if negative number is present in string or
                return sum

                Required Params:
                    delimiter_regex : regex to match delimiters
                    numbers_string : input string containing numbers
            """
            # parse the numbers in the input string to ints
            numbers = list(map(int, re.split(delimiters_regex, numbers_string)))
            # filter to the negative numbers in the parsed numbers
            negative_numbers = list(filter(lambda x: x<0, numbers))
            # if any negative numbers are present
            if len(negative_numbers)>0:
                # raise exception with list of negative numbers
                raise(Exception('Negatives not allowed ['+','.join(map(str, negative_numbers))+']'))
            else:
                # return the sum of numbers in input string
                return sum(numbers)

        # parse the comma seperated numbers into ints, sum them and return sum
        return neg_except_or_sum(delimiters_regex, numbers_string)
