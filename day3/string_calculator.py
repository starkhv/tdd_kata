import re
import pdb

def add(numbers_string):
    """Add the numbers in numbers_string and return the sum
    """
    # delimiter declared regex 
    dd_reg = re.compile(r'//(?P<delimiter>.*)\n(?P<numbers_string>.*)')
    # delimiter declared regex match 
    dd_match = re.match(dd_reg, numbers_string)
    if dd_match:
        # delimiter declared regex group dict
        dd_reg_groups = dd_match.groupdict()
        delimiters = [dd_reg_groups['delimiter']]
        numbers_string = dd_reg_groups['numbers_string']
    else:
        delimiters = [',', '\n']
    delimiters_regex = re.compile(r'|'.join(map(re.escape, delimiters)))
    if len(numbers_string)>0:
        def is_negative(numbers):
            """ Raise exception if any number is negative, else return original list
            """
            neg_numbers = []
            for number in numbers:
                number = int(number)
                if number < 0:
                    neg_numbers.append(number)
            if len(neg_numbers)>0:
                raise(Exception('negatives not allowed ['+\
                        (', '.join(map(str, neg_numbers)+']'))))
            else:
                return numbers
        numbers = list(map(int, re.split(delimiters_regex, numbers_string)))
        numbers = is_negative(numbers)
        return sum(numbers)
    else:
        return 0
