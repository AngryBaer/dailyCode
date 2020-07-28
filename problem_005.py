# Daily Coding Problem 5

"""
    cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

    Given this implementation of cons:

    def cons(a, b):
        def pair(f):
            return f(a, b)
        return pair

    Implement car and cdr.
"""


# -------------------------------------------------------------------------------------------------------------------- #
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    """
    return first element
    :param pair:
    :return result:
    """
    return pair(lambda a, b: a)


def cdr(pair):
    """
    return last element
    :param pair:
    :return result:
    """
    return pair(lambda a, b: b)


# -------------------------------------------------------------------------------------------------------------------- #
if __name__ == "__main__":
    print car(cons(3, 4))
    print cdr(cons(3, 4))
# -------------------------------------------------------------------------------------------------------------------- #
