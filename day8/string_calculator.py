import re

def add(numbers_string):
    # if not empty string
    if len(numbers_string)>0:
        # delimiter declaration regex
        dd_regex = re.compile(r'//(?P<delimiter>.*)\n(?P<numbers_string>.*)')
        # check if given string contains delimiter declaration
        dd_match = re.match(dd_regex, numbers_string)
        if dd_match:
            # dictionary of delimiter declaration regex groups
            dd_dict = dd_match.groupdict()
            # list of delimiters
            delimiters = [dd_dict['delimiter']]
            # overwrite the numbers_string with parsed one
            numbers_string = dd_dict['numbers_string']
        else:
            # list of delimiters
            delimiters = [',', '\n']
        # regex of all delimiters
        delimiters_regex = re.compile(r'|'.join(delimiters))
        def neg_or_sum(numbers_string):
            """If negative numbers are present in numbers_string raise exception
               else return the sum of numbers"""
            # list of numbers(ints)
            numbers = list(map(int, re.split(delimiters_regex, numbers_string)))
            # filter non-negative numbers
            neg_numbers = list(filter(lambda x: x<0, numbers))
            if len(neg_numbers)>0:
                raise(Exception('negatives not allowed [' + ','.join(map(str, neg_numbers)) + ']'))
            else:
                return sum(numbers)
        # split with delimiters regex and return sum
        return neg_or_sum(numbers_string)
    else:
        # return zero for empty string
        return 0
