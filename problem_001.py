# Daily Coding Problem 1

"""
    Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

    For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

    Bonus: Can you do this in one pass?
"""


# -------------------------------------------------------------------------------------------------------------------- #
def add_to_k(input_list, k):

    sums = set()

    for i in input_list:

        if k - i in sums:
            return True

        sums.add(i)

    return False


# -------------------------------------------------------------------------------------------------------------------- #
if __name__ == "__main__":

    input_list = [10, 15, 3, 7]
    k = 17

    print add_to_k(input_list, k)
# -------------------------------------------------------------------------------------------------------------------- #
