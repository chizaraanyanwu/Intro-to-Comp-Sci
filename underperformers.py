"""Functions to demonstrate testing with and without mutation."""


def collect_underperformers(nums: list[int], threshold: int) -> list[int]:
    """Return a new list consisting of those numbers in nums that are below
    threshold, in the same order as in nums.

    >>> collect_underperformers([], 7)  # empty
    []
    >>> collect_underperformers([7], 7)  # 1 element: not included
    []
    >>> collect_underperformers([5], 7)  # 1 element: included
    [5]
    >>> collect_underperformers([1, 3, 2, 4], 5)  # all included
    [1, 3, 2, 4]
    >>> collect_underperformers([4, 3, 1, 2], 1)  # none included
    []
    >>> collect_underperformers([1, 4, 3, 2], 3)  # some included
    [1, 2]
    """

    result = []
    for item in nums:
        if item < threshold:
            result.append(item)
    return result


def keep_underperformers(nums: list[int], threshold: int) -> None:
    """Modify nums to only contain those numbers in nums that are below
    threshold, in the same order as in nums.

    >>> nums = []
    >>> keep_underperformers(nums, 7)  # empty
    >>> nums
    []
    >>> nums = [7]
    >>> keep_underperformers(nums, 7)  # 1 element: not included
    >>> nums
    []
    >>> nums = [5]
    >>> keep_underperformers(nums, 7)  # 1 element: included
    >>> nums
    [5]
    >>> nums = [1, 3, 2, 4]
    >>> keep_underperformers(nums, 5)  # all included
    >>> nums
    [1, 3, 2, 4]
    >>> nums = [4, 3, 1, 2]
    >>> keep_underperformers(nums, 1)  # none included
    >>> nums
    []
    >>> nums = [1, 4, 3, 2]
    >>> keep_underperformers(nums, 3)  # some included
    >>> nums
    [1, 2]
    """

    index = 0
    while index < len(nums):
        if nums[index] >= threshold:
            del nums[index]
        else:
            index = index + 1


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
