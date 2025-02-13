"""
    Daily Coding Problem 9:

    Given a list of integers, write a function that returns the largest sum of non-adjacent
    numbers. Numbers can be 0 or negative.

    For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should
    return 10, since we pick 5 and 5.

    Follow-up: Can you do this in O(N) time and constant space?
"""


# ----------------------------------------------------------------------------------------------- #
def largest_non_adjacent_recursive(input_list: list) -> int:
    if not input_list:
        return 0

    return max(
        largest_non_adjacent_recursive(input_list[1:]),
        input_list[0] + largest_non_adjacent_recursive(input_list[2:])
    )


def largest_non_adjacent(input_list: list) -> int:
    if len(input_list) <= 2:
        return max(0, input_list)

    max_excluding_last = max(0, input_list[0])
    max_including_last = max(max_excluding_last, input_list[1])

    for item in input_list[2:]:
        max_including_last_temp = max_including_last
        max_including_last = max(max_including_last, max_excluding_last + item)
        max_excluding_last = max_including_last_temp

    return max(max_including_last, max_excluding_last)


if __name__ == "__main__":
    TEST_LIST1 = [2, 4, 6, 2, 5]
    TEST_LIST2 = [5, 1, 1, 5]

    assert largest_non_adjacent_recursive(TEST_LIST1) == 13
    assert largest_non_adjacent_recursive(TEST_LIST2) == 10

    assert largest_non_adjacent(TEST_LIST1) == 13
    assert largest_non_adjacent(TEST_LIST2) == 10
# ----------------------------------------------------------------------------------------------- #
