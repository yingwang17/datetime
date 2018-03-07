'''
    Advanced Python - Session 3 homework
    Author:  Ying Wang yingwang1@gmail.com
    Last modified:    2018-03-04
'''


import datetime
from functools import reduce

# initializing a new datetime.date object
def get_date_object(date = None):

    if not date:
        return datetime.datetime.today().date()

    else:
        is_valid = False
        for fmt in ('%Y-%m-%d', '%d.%m.%Y', '%m/%d/%Y', '%d-%b-%y', '%Y/%m/%d', '%m/%d/%y', '%m-%d-%Y'):
            try:
                return datetime.datetime.strptime(date, fmt).date()
                is_valid = True
            except ValueError:
                pass

        if is_valid == False:
            raise ValueError("Please enter a valid date")


#return a formatted date string
def get_date_string (date_object = None):

    if not date_object:
        return datetime.datetime.today().strftime('%Y-%m-%d')

    else:
        try:
            return date_object.strftime('%Y-%m-%d')

        except (TypeError, ValueError, AttributeError):
            raise TypeError('please enter an valid date object')


# return a formatted date string
def get_date_string (date_object = None, format = 'MM/DD/YYYY'):

    if not date_object:
        return datetime.datetime.today().strftime('%Y-%m-%d')

    else:
        try:
            rpls = ('YYYY','%Y'), ('MM','%m'), ('DD','%d'), ('Mon','%b'), ('YY','%y')
            fmt_converted = reduce(lambda a, b: a.replace(*b), rpls, format)

            # check if regular format (start with %)
            if fmt_converted.find('%') == 0:
                return date_object.strftime(fmt_converted)
            else:
                raise ValueError

        except (TypeError, ValueError, AttributeError):
            raise ValueError('Please enter an valid date object!')


#advancing the date
def add_day (dt, ds = 0):

    try:
        return dt + datetime.timedelta(days = ds)
    except (TypeError, ValueError):
        raise ValueError('please enter an date object and integer as days of advancing')


#advancing the weeks
def add_week (dt, ws = 0):

    try:
        return dt + datetime.timedelta(weeks = ws)
    except (TypeError, ValueError):
        raise TypeError('please enter an date object and integer as weeks of advancing')


def add_month (dt):
    try:
        new_d = datetime.datetime(year = dt.year, month = dt.month+1, day = dt.day).date()

    except (IndexError, ValueError):
        dt_new = add_day(dt, -1)
        new_d = datetime.datetime(year=dt_new.year, month=dt_new.month + 1, day=dt_new.day).date()

    return new_d

def add_year (dt):
    try:
        new_d = datetime.datetime(year = dt.year+1, month = dt.month, day = dt.day).date()

    except ValueError:
        dt_new = add_day(dt, -1)
        new_d = datetime.datetime(year=dt_new.year+1, month=dt_new.month, day=dt_new.day).date()

    return new_d














