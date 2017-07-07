import re

def add(numbers_string):
    if len(numbers_string)>0:
        # delimiter declaration regex
        dd_regex = re.compile(r'//(?P<delimiter>.*)\n(?P<numbers_string>.*)')
        # check if given string matches delimiter declaration regex
        dd_match = re.match(dd_regex, numbers_string)
        if dd_match:
            # delimiter declaration regex group dictionary
            dd_dict = dd_match.groupdict()
            # list of delimiters
            delimiters = [dd_dict['delimiter']]
            # parsed numbers string
            numbers_string = dd_dict['numbers_string']
        else:
            # list of delimiters
            delimiters = [',', '\n']
        # regex of delimiters
        delimiters_regex = re.compile(r'|'.join(map(re.escape, delimiters)))
        # split numbers string into numbers based on delimiters regex
        numbers = list(map(int, re.split(delimiters_regex, numbers_string)))
        def neg_or_sum(numbers):
            """Raise exception if negative numbers are present else return sum"""
            # list of negative numbers in numbers
            neg_numbers = list(filter(lambda x: x<0, numbers))
            # if negative numbers are present then raise exception with list of negative numbers
            if len(neg_numbers)>0:
                raise(Exception('negatives not allowed ['+','.join(map(str, neg_numbers))+']'))
            else:
                return sum(numbers)
        return neg_or_sum(numbers)
    else:
        return 0
