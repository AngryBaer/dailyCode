"""
    Daily Coding Problem 1:

    Given a list of numbers and a number k, return whether any two numbers from the list add up
    to k. For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

    Bonus: Can you do this in one pass?
"""


# ----------------------------------------------------------------------------------------------- #
def add_to_k(input_list: list, k: int) -> bool:
    """ Two number in the list add up to k? """
    sums = set()

    for i in input_list:
        if k - i in sums:
            return True

        sums.add(i)

    return False
# ----------------------------------------------------------------------------------------------- #


# ----------------------------------------------------------------------------------------------- #
if __name__ == "__main__":
    TEST_LIST = [10, 15, 3, 7]
    TEST_INT = 17

    assert add_to_k(TEST_LIST, TEST_INT) is True
# ----------------------------------------------------------------------------------------------- #
