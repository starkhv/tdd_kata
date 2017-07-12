import re

def add(numbers_string):
    if len(numbers_string)>0:
        # delimiter declaration regex
        dd_regex = re.compile(r'//(?P<delimiter>.*)\n(?P<numbers_string>.*)')
        # try to match numbers_string with dd_regex
        dd_match = re.match(dd_regex, numbers_string)
        if dd_match:
            # groups matched in delimiter declaration
            dd_groups = dd_match.groupdict()
            delimiter = dd_groups['delimiter']
            numbers_string = dd_groups['numbers_string']
            delimiters = [delimiter]
        else:
            delimiters = [',', '\n']
        delimiter_string = '|'.join(map(re.escape, delimiters))
        def neg_or_sum(numbers_string):
            """Raise exception if negatives are present, else return sum"""
            # parse ints of numbers in numbers_string
            numbers = list(map(int, re.split(delimiter_string, numbers_string)))
            # list of negative numbers
            neg_numbers = list(filter(lambda x: x < 0, numbers))
            if len(neg_numbers)>0:
                raise(Exception('negatives not allowed ['+', '.join(map(str, neg_numbers))+']'))
            else:
                return sum(numbers)
        return neg_or_sum(numbers_string)
    else:
        return 0
