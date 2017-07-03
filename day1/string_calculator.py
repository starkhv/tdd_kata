import pdb
import re

def add(numbers):
    '''Add the numbers in comma delimited string numbers

    Params:
        numbers: comma delimited string

    Returns sum of all numbers
    '''
    # delimiter declaration pattern
    delimiter_declaration = re.compile(r'//\[?(?P<delimiter>.*?)\]?\n(?P<numbers_string>.*)')
    # match object for delimiter declaration
    match_declaration = re.match(delimiter_declaration, numbers)
    # if it is a match declaration get the numbers string and delimiters
    if match_declaration:
        numbers = match_declaration.groupdict()['numbers_string']
        delimiters = match_declaration.groupdict()['delimiter']
        # multiple delimiters pattern
        multiple_delimiters_pattern = re.compile(r'\]\[')
        delimiters = re.split(multiple_delimiters_pattern, delimiters)
    else:
        # set of delimiters
        delimiters = set(['\n', ','])
    # compiled regex to split using multiple delimiters
    delimiters_regex = re.compile('|'.join(map(re.escape, delimiters)))
    numbers = re.split(delimiters_regex, numbers)
    # convert to int after checking non-negative
    def non_neg_to_int(number):
        # handle empty string
        if len(number)==0:
            return 0
        number = int(number)
        if number < 0:
            raise Exception('negatives not allowed')
        else:
            return number
    # filter numbers greater than 1000
    def filter_numbers_gt_1000(numbers):
        numbers_int = map(non_neg_to_int, numbers)
        numbers_int = filter(lambda x: x<1000, numbers_int)
        return numbers_int
    numbers_int = filter_numbers_gt_1000(numbers)
    return sum(numbers_int)
