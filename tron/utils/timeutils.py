"""Time utilites"""
import datetime
import re
import time


# Global time override
_current_time_override = None


def override_current_time(current_time):
    """Interface for overriding the current time

    This is a test hook for forcing the app to think it's a specific time.
    """
    global _current_time_override
    _current_time_override = current_time


def current_time():
    """Standard interface for generating the current time."""
    if _current_time_override is not None:
        return _current_time_override
    else:
        return datetime.datetime.now()


def current_timestamp():
    return to_timestamp(current_time())


def to_timestamp(time_val):
    """Generate a unix timestamp for the given datetime instance"""
    return time.mktime(time_val.timetuple())


def macro_timedelta(start_date, years=0, months=0, days=0):
    """Since datetime doesn't provide timedeltas at the year or month level,
    this function generates timedeltas of the appropriate sizes.
    """
    delta = datetime.timedelta(days=days)

    new_month = start_date.month + months
    while new_month > 12:
        new_month -= 12
        years += 1
    while new_month < 1:
        new_month += 12
        years -= 1

    end_date = datetime.datetime(start_date.year + years,
                                 new_month, start_date.day)
    delta += end_date - start_date

    return delta


def duration(start_time, end_time=None):
    """Get a timedelta between end_time and start_time, where end_time defaults
    to now().
    """
    if not start_time:
        return None
    last_time = end_time if end_time else current_time()
    return last_time - start_time


class DateArithmetic(object):
    """Parses a string which contains a date arithmetic pattern and returns
    a date with the delta added or subtracted.
    """

    DATE_TYPE_PATTERN = re.compile(r'(\w+)([+-]\d+)?')

    DATE_FORMATS = {
        'year':                 '%Y',
        'month':                '%m',
        'day':                  '%d',
        'shortdate':            '%Y-%m-%d'
    }

    @classmethod
    def parse(cls, date_str, dt=None):
        """Parse a date arithmetic pattern (Ex: 'shortdate-1'). Supports
        date strings: shortdate, year, month, day, unixtime, daynumber.
        Supports subtraction and addition operations of integers. Time unit is
        based on date format (Ex: seconds for unixtime, days for day).
        """
        dt = dt or current_time()
        match = cls.DATE_TYPE_PATTERN.match(date_str)
        if not match:
            return
        attr, value = match.groups()
        delta = int(value) if value else 0

        if attr in ('shortdate', 'year', 'month', 'day'):
            if delta:
                kwargs = {'days' if attr == 'shortdate' else attr + 's': delta}
                dt += macro_timedelta(dt, **kwargs)
            return dt.strftime(cls.DATE_FORMATS[attr])

        if attr == 'unixtime':
            return int(to_timestamp(dt)) + delta

        if attr == 'daynumber':
            return dt.toordinal() + delta
