"""
    Daily Coding Problem 4:

    Given an array of integers, find the first missing positive integer in linear time and constant
    space. In other words, find the lowest positive integer that does not exist in the array.
    The array can contain duplicates and negative numbers as well.

    For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

    You can modify the input array in-place.
"""


# ----------------------------------------------------------------------------------------------- #
def solution_1(input_list: list) -> int:
    max_value = max(input_list) + 1

    for i in range(1, max_value):
        if i not in input_list:
            return i

    return max_value


def solution_2(input_list: list) -> int:
    i = 1

    while i in set(input_list):
        i += 1

    return i
# ----------------------------------------------------------------------------------------------- #


# ----------------------------------------------------------------------------------------------- #
if __name__ == "__main__":
    TEST_LIST1 = [3, 4, -1, 1]
    TEST_LIST2 = [1, 2, 0]

    assert solution_1(TEST_LIST1) == 2
    assert solution_1(TEST_LIST2) == 3

    assert solution_2(TEST_LIST1) == 2
    assert solution_2(TEST_LIST2) == 3
# ----------------------------------------------------------------------------------------------- #
