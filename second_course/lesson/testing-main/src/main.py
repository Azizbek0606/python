def sum_(x: int, y: int) -> int:
    """
    This function returns the sum of two integers
    >>> sum_(1, 1)
    :param x: int
    :param y: int
    :return: int | TypeError
    """
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Arguments must be integers")
    return x + y


def minus(x: int, y: int) -> int:
    """
    This function returns the difference of two integers
    >>> minus(1, 1)
    :param x: int
    :param y: int
    :return: int | TypeError
    """
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Arguments must be integers")
    return x - y
