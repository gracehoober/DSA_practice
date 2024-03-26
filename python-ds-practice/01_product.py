def product(a, b):
    """Return product of a and b.

        >>> product(2, 2)
        4

        >>> product(2, -2)
        -4

        >>> product("a", 4)
        "The input values provided must be numbers."
    """
    if type(a) != "number" or type(b) != "number":
        return "The input values provided must be numbers."
    else:
        return a * b
    