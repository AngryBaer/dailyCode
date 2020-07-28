# Daily Coding Problem 4

"""
    Given an array of integers, find the first missing positive integer in linear time and constant space. In other
    words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and
    negative numbers as well.

    For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

    You can modify the input array in-place.
"""


# -------------------------------------------------------------------------------------------------------------------- #
def solution_1(input_list):

    max_value = max(input_list) + 1

    for i in range(1, max_value):
        if i not in input_list:
            return i

    return max_value


def solution_2(input_list):

    unique_values = set(input_list)
    i = 1

    while i in unique_values:
        i += 1

    return i


# -------------------------------------------------------------------------------------------------------------------- #
if __name__ == "__main__":

    input_list_1 = [3, 4, -1, 1]
    input_list_2 = [1, 2, 0]

    print
    print solution_1(input_list_1)
    print solution_1(input_list_2)

    print
    print solution_2(input_list_1)
    print solution_2(input_list_2)
# -------------------------------------------------------------------------------------------------------------------- #
