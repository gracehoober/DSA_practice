def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    phrase_to_list = list(phrase)
    phrase_to_list.reverse()
    back_to_phrase = "".join(phrase_to_list)
    return back_to_phrase
