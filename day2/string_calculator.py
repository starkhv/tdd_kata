import pdb
import re

def add(numbers_string):
    # delimiter declaration regex
    dd_regex = r'//(?P<delimiter>.*)\n(?P<numbers_string>.*)'
    # delimiter declaration match
    dd_match = re.match(dd_regex, numbers_string)
    if dd_match:
        group_dict = dd_match.groupdict()
        delimiters = [group_dict['delimiter']]
        numbers_string = dd_match.groupdict()['numbers_string']
    else:
        delimiters = [',', '\n']
    delimiter_regex = '|'.join(map(re.escape, delimiters))
    if len(numbers_string)>0:
        def convert_nonnegative_to_int(number):
            number = int(number)
            if number<0:
                raise(Exception('negatives not allowed ' + str(number)))
            else:
                return number
        numbers = map(convert_nonnegative_to_int, re.split(delimiter_regex, numbers_string))
        return sum(numbers)
    else:
        return 0
