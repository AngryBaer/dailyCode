# Daily Coding Problem 2

"""
    This problem was asked by Uber.

    Given an array of integers, return a new array such that each element at index i of the new array is the product of
    all the numbers in the original array except the one at i.

    For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was
    [3, 2, 1], the expected output would be [2, 3, 6].

    Follow-up: what if you can't use division?
"""


import numpy


# -------------------------------------------------------------------------------------------------------------------- #
def solution_1(arguments):
    return [numpy.product(arguments)/x for x in arguments]


def solution_2(arguments):

    result_list = []

    for n, i in enumerate(arguments):
        temp_list = arguments[:]
        temp_list.pop(n)

        result_list.append(numpy.product(temp_list))

    return result_list


# -------------------------------------------------------------------------------------------------------------------- #
if __name__ == "__main__":
    input_list_1 = [1, 2, 3, 4, 5]
    input_list_2 = [3, 2, 1]

    print
    print "with division"
    print input_list_1, solution_1(input_list_1)
    print input_list_2, solution_1(input_list_2)

    print
    print "without division:"
    print input_list_1, solution_2(input_list_1)
    print input_list_2, solution_2(input_list_2)

# -------------------------------------------------------------------------------------------------------------------- #
