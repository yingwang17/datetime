#!/usr/bin/env python

import date_simple as ds
import datetime as dt
import pytest

DATEOBJ_TODAY = dt.datetime.today().date()
DATEOBJ_DAY = dt.datetime(2018,2,26,0,0).date()
STR_TODAY = '2018-03-04'
STR_DAY = '2018-02-26'
STR_DAY2 = '02/26/2018'
STR_DAY3 = '26-Feb-18'


def test_get_date_object():
    dateobj1 = ds.get_date_object()
    assert dateobj1 == DATEOBJ_TODAY

def test_get_date_object():
    dateobj2 = ds.get_date_object(date='2018-02-26')
    assert dateobj2 == DATEOBJ_DAY

def test_get_date_object():
    with pytest.raises(ValueError):
        dateobj2 = ds.get_date_object(date='bad date')


def test_get_date_string():
    datestr = ds.get_date_string()
    assert datestr == STR_TODAY

def test_get_date_string():
    datestr = ds.get_date_string(date_object= DATEOBJ_DAY)
    assert datestr == STR_DAY

def test_get_date_string():
    with pytest.raises(TypeError):
        datestr = ds.get_date_string(date_object= 'not_a_date_object')


#Extra Credit
def test_get_date_string():
    datestr = ds.get_date_string(date_object = DATEOBJ_DAY, format = 'MM/DD/YYY')
    assert datestr == STR_DAY2

def test_get_date_string():
    datestr = ds.get_date_string(date_object = DATEOBJ_DAY, format = 'DD-Mon-YY')
    assert datestr == STR_DAY3

def test_get_date_string():
    with pytest.raises(ValueError):
        datestr = ds.get_date_string(date_object = DATEOBJ_DAY, format = 'unrecognized format')



