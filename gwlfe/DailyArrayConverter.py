import random

import numpy.ma as ma
# from numba import jit
from numpy import array
from numpy import r_
from numpy import ravel
from numpy import where
from numpy import zeros

leap_year = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             True, True, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, True, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, True, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, True, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False, False, True, False, False, False, False,
             False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False, False, False, False]
non_leap_year = [False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, True, True, True, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, True, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, True, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, True, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False, True,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False]


def mask_builder(DaysMonth):
    ones = ravel(ones((12, 31))).astype("int")
    slices = []
    for i, month in enumerate(DaysMonth[0]):
        slices.append(slice(31 * i, 31 * i + month))
    ones[r_[tuple(slices)]] = 0
    return ones


def ymd_to_daily(ymd_array, DaysMonth):
    month_maps = [leap_year if x[1] == 29 else non_leap_year for x in DaysMonth]
    mask = ravel(array(month_maps))
    x = ma.array(ymd_array, mask=mask)
    return x[~x.mask]


def daily_to_ymd(daily_array, NYrs, DaysMonth):
    result = zeros((NYrs * 12 * 31,))
    month_maps = [leap_year if x[1] == 29 else non_leap_year for x in DaysMonth]
    mask = ravel(array(month_maps))
    x = ma.array(result, mask=mask)
    x[~x.mask] = daily_array
    return x.reshape((NYrs, 12, 31))


def ymd_to_daily_slow(ymd_array, NYrs, DaysMonth):
    result = []
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                result.append(ymd_array[Y][i][j])
    return array(result)


def get_value_for_yesterday(variable, variable_0, Y_in, i_in, j_in, DaysMonth):
    temp = array(variable)
    key = random.randint(100000000000, 999999999999)  # use something that is hopefully unique so we can find it again
    temp[Y_in, i_in, j_in] = key
    temp = ymd_to_daily(temp, DaysMonth)
    today = where(temp == key)[0]
    if (len(today) != 1):
        raise AssertionError("this array has values equal to the key")

    if (today[0] - 1 >= 0):
        return temp[today[0] - 1]
    else:  # at the first index of the array
        return variable_0
