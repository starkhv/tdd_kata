import re

def add(numbers_string):
    if len(numbers_string)>0:
        # delimiter declaration regex
        dd_regex = re.compile(r'//(?P<delimiter>.*)\n(?P<numbers_string>.*)')
        # match object for delimiter declaration
        dd_match = re.match(dd_regex, numbers_string)
        # check if delimiter is declared
        if dd_match:
            # get groups dict
            dd_dict = dd_match.groupdict()
            # make delimiters list
            delimiters = [dd_dict['delimiter']]
            # overwrite numbers_string
            numbers_string = dd_dict['numbers_string']
        else:
            # list of delimiters
            delimiters = [',', '\n']
        # regex of delimiters
        delimiters_regex = re.compile(r'|'.join(map(re.escape, delimiters)))
        def neg_except_or_sum(numbers_string, delimiters_regex):
            """Raise exception if negative number is present, else return sum"""
            # parse numbers into a list
            numbers = list(map(int, re.split(delimiters_regex, numbers_string)))
            # filter negative numbers
            neg_numbers = list(filter(lambda x: x<0, numbers))
            if len(neg_numbers)>0:
                raise(Exception('negatives not allowed [' + ','.join(map(str, neg_numbers)) + ']'))
            else:
                return sum(numbers)
        return neg_except_or_sum(numbers_string, delimiters_regex)
    else:
        return 0
