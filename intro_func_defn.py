"""Code for week 2 worksheets: starter code.
"""


def add_bonus(grade: float, bonus: float) -> float:
    """Return the result of adding bonus to grade, capped at 100.0.

    >>> add_bonus(67.0, 10.0)
    77.0
    >>> add_bonus(92.5, 9.0)
    100.0
    """

    return min(grade + bonus, 100.0)  # replace this line with your solution


# def percentage(num: int, out_of: int) -> int:
#     """Return what percent num is of out_of, rounded to an int
#     (using the function round for rounding).

#     >>> percentage(10, 200)
#     ???
#     >>> percentage(151, 300)
#     ???
#     """

#     pass  # replace this line with your solution


# def max_of_min(num1: float, num2: float, val1: float, val2: float) -> float:
#     """Return the maximum of the minimums of the pairs num1 and num2,
#     and val1 and val2.

#     >>> ???
#     ???
#     >>> ???
#     ???
#     """

#     pass  # replace this line with your solution


if __name__ == '__main__':
    import doctest
    doctest.testmod()
