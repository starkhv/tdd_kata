import re

def add(numbers_string):
    if len(numbers_string)>0:
        # delimiter declaration regex
        dd_regex = re.compile(r'//(?P<delimiter>.*)\n(?P<numbers_string>.*)')
        # match delimiter declaration with numbers_string
        dd_match = re.match(dd_regex, numbers_string)
        # if delimiter declaration pattern is present in numbers_string
        if dd_match:
            # parse regex groups in delimiter declaration regex into dict
            dd_groups = dd_match.groupdict()
            # list of delimiters
            delimiters = [dd_groups['delimiter']]
            # overwrite numbers_string with parsed numbers_string from delimiter declaration
            numbers_string = dd_groups['numbers_string']
        else:
            # use default delimiters
            delimiters = [',', '\n']
        delimiters_regex = re.compile(r'|'.join(map(re.escape, delimiters)))
        def neg_except_or_sum(numbers_string, delimiters_regex):
            """Raise exception if negative number is present in string, else return sum """
            # parse ints of numbers in numbers_string
            numbers = list(map(int, re.split(delimiters_regex, numbers_string)))
            # filter to negative numbers
            neg_numbers = list(filter(lambda x: x<0, numbers))
            # if negative numbers are present
            if len(neg_numbers)>0:
                raise(Exception('negatives not allowed ['+','.join(neg_numbers)+']'))
            else:
                return sum(numbers)
        return neg_except_or_sum(numbers_string, delimiters_regex)
    else:
        return 0
