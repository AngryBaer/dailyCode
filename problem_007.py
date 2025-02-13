"""
    Daily Coding Problem 7:

    Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it
    can be decoded.

    For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and
    'ak'.

    You can assume that the messages are decodable. For example, '001' is not allowed.
"""
import re
from collections import defaultdict


MAPPING = {str(value + 1): chr(ord('a') + value) for value in range(0, 26)}


# ----------------------------------------------------------------------------------------------- #
def flatten_list(list_object):
    for items in list_object:
        if isinstance(items, list):
            yield from flatten_list(items)
        else:
            yield items


def find_combinations(code):
    combinations = []

    for key in MAPPING:
        re_object = re.compile(f'(?={key})')
        matches = re_object.finditer(code) or []

        for match in matches:
            combinations.append((len(key), match.start(), MAPPING[key]))

    return combinations


def encode(input_string):
    encoded_list = []
    combinations = find_combinations(input_string)

    if not combinations:
        return input_string

    for item in combinations:
        elements = list(input_string)
        del elements[item[1]:item[1] + item[0]]
        elements.insert(item[1], item[2])

        result = encode(''.join(elements))
        encoded_list.append(result)

    return encoded_list


def num_encodings(code):
    cache = defaultdict(int)
    cache[len(code)] = 1

    for i in reversed(range(len(code))):
        if code[i].startswith('0'):
            cache[i] = 0
        elif i == len(code) - 1:
            cache[i] = 1
        else:
            if int(code[i:i + 2]) <= len(MAPPING):
                cache[i] = cache[i + 2]

            cache[i] += cache[i + 1]

    return cache[0]
# ----------------------------------------------------------------------------------------------- #


# ----------------------------------------------------------------------------------------------- #
if __name__ == "__main__":
    print(sorted(list(set(flatten_list(encode('111'))))))
    assert num_encodings('111') == 3
# ----------------------------------------------------------------------------------------------- #
