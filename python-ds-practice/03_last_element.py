def last_element(lst):
    """Return last item in list or None if list is empty.

        >>> nums = [1, 2, 3]
        >>> last_element(nums)
        3
        >>> last_element([]) is None
        True

    Make sure original list has not been mutated:

        >>> nums == [1, 2, 3]
        True
    """

    return lst[len(lst) - 1] if len(lst) > 0 else None