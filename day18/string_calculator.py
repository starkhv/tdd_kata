# built-in modules
import re

def add(numbers_string):
    """ Add numbers in given string and return sum """
    # if numbers_string is not empty
    if len(numbers_string) > 0:
        # regex to detect delimiter declaration in numbers_string
        dd_regex = re.compile(r'//(?P<delimiter>.*)\n(?P<numbers_string>.*)')
        # try matching dd_regex in numbers_string
        dd_match = re.match(dd_regex, numbers_string)
        # if delimiter is declared
        if dd_match:
            # map groups in delimiter declaration to a dictionary
            dd_groups_dict = dd_match.groupdict()
            # make delimiters list from the parsed delimiter
            delimiters = [dd_groups_dict['delimiter']]
            # overwrite numbers_string with the parsed one
            numbers_string = dd_groups_dict['numbers_string']
        # without delimiter declaration in numbers_string
        else:
            # use default list of delimiters
            delimiters = [',', '\n']

        # regex of delimiters
        delimiters_regex = re.compile(r'|'.join(map(re.escape, delimiters)))

        def neg_except_or_sum(numbers_string, delimiters_regex):
            """ Raise exception with list of negative numbers if any are present in numbers_string
                Return sum of the numbers otherwise
            """
            # parse ints of numbers form string
            numbers = list(map(int, re.split(delimiters_regex, numbers_string)))
            # filter negative numbers to a list
            neg_numbers = list(filter(lambda x: x<0, numbers))
            # if any negative numbers are present
            if len(neg_numbers)>0:
                # raise exception containing the list of negative numbers
                raise(Exception('negatives not allowed ['+','.join(map(str, neg_numbers))+']'))
            else:
                # return sum of the numbers
                return sum(numbers)

        return neg_except_or_sum(numbers_string, delimiters_regex)
    # if numbers_string is empty
    else:
        return 0
