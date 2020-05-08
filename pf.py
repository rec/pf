from datetime import datetime

DATE_FORMAT = '%Y/%m/%d:%H:%M:%S/%f'


def string_to_date(s):
    return datetime.strptime(s, DATE_FORMAT)


def date_to_string(dt):
    return dt.strftime(DATE_FORMAT)
