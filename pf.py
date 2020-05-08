from datetime import datetime

DATE_FORMAT = '%Y/%m/%d %H:%M:%S.%f'
# Includes ms so the roundtrip test works.  I will probably turn that off for
# the test.

DOLLARS_FORMAT_ERROR = (
    'Dollars must either be a whole number or have exactly two decimal places'
)


# it is a crime against nature to use floating point for calculations on money.
# Represent money in whole number cents for these exercises.

def string_to_cents(s):
    """
    Convert a string representing a dollar value into a whole number of cents.

    Inputs are either whole numbers (100, -123) or numbers with exactly two
    digits after the decimal place (100.23, -123.05).
    """
    dollars, *cents = s.split('.')

    if len(cents) > 1:
        raise ValueError(DOLLARS_FORMAT_ERROR)

    cents = cents[0] if cents else '00'
    if len(cents) != 2 or not cents.isnumeric():
        raise ValueError(DOLLARS_FORMAT_ERROR)

    try:
        return 100 * int(dollars) + int(cents)
    except ValueError:
        raise ValueError(DOLLARS_FORMAT_ERROR)


def cents_to_string(cents):
    """
    Convert an integer number of cents into a string representing a dollar
    value.
    """
    return '%d.%02d' % divmod(cents, 100)


def string_to_date(s):
    return datetime.strptime(s, DATE_FORMAT)


def date_to_string(dt):
    """"
    Converts a datetime to a string.

    ARGUMENTS
      dt: a datetime
    """
    return dt.strftime(DATE_FORMAT)
