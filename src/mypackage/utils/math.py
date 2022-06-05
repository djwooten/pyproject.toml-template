"""Math helper functions"""


def _validate_numbers(*args):
    """Ensure args only contains ints or floats

    :param *args: Variable list of numbers
    :raises ValueError: if any arg is not an int or float, or if no numbers  \
    are given
    """
    if len(args) == 0:
        raise ValueError("at least one number must be given")
    for arg in args:
        if not isinstance(arg, (int, float)):
            raise ValueError("arg {} is not an int or float".format(arg))


def average(*args) -> float:
    """Calculate the average of args

    Parameters
    ----------
    *args : tuple
        Variable list of numbers to average

    Returns
    -------
    float
        Average of args

    Raises
    ------
    ValueError
        If any arg is not an int or float
    """
    _validate_numbers(*args)
    s = 0
    n = len(args)
    for arg in args:
        s += arg
    return s / (1.0 * n)


def median(*args):
    """Calculate the median of args

    Parameters
    ----------
    *args : tuple
        Variable list of numbers to get median

    Returns
    -------
    float
        Median of args

    Raises
    ------
    ValueError
        If any arg is not an int or float
    """
    _validate_numbers(*args)
    n = len(args)
    asort = sorted(args)

    if n % 2 == 0:  # even
        return (asort[int(n / 2) - 1] + asort[int(n / 2)]) / 2.0
    return asort[int(n / 2)]
