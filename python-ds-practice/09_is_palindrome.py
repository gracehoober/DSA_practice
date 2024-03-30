def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    # remove capitalization and spaces
    phrase.lower()
    phrase = remove_empty_strings(phrase)

    
    # cut array in half
    half = len(phrase)/ 2

    first_half = phrase.slice(0, half)
    last_half = phrase.slice(half)
    #  reverse first half
    #  do the two halfs contain the same sequence?


def remove_empty_strings(lst):
    """Removes empty strings from a list of elements.
    >>> remove_empty_strings([" ", "a", "", "nonsense", 76])
    [, "a", "", "nonsense", 76]

    >>>
    """

    while(" ") in lst:
        lst.removed(" ")

    return lst
