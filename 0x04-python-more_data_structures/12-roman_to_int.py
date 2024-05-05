#!/usr/bin/python3
def roman_to_int(roman_string):
    """converts a Roman numeral to an integer."""
    result = 0
    v = 0
    c = 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500,
                  'M': 1000}
    if roman_string is None:
        return 0
    for i in roman_string:
        if roman_dict.get(i) is None:
            return 0
        result += roman_dict[i]
        if roman_dict[i] > v and c != 0:
            result -= 2 * v
        v = roman_dict[i]
        c += 1
    return result
