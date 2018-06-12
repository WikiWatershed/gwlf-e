import random

import numpy.ma as ma
from numpy import array
from numpy import r_
from numpy import ravel
from numpy import where
from numpy import zeros
# from numba import jit

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
    month_maps = map(lambda x: leap_year if x[1] == 29 else non_leap_year, DaysMonth)
    mask = ravel(array(month_maps))
    x = ma.array(ymd_array, mask=mask)
    return x[~x.mask]


def daily_to_ymd(daily_array, NYrs, DaysMonth):
    result = zeros((NYrs * 12 * 31,))
    month_maps = map(lambda x: leap_year if x[1] == 29 else non_leap_year, DaysMonth)
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

# @jit(cache=True, nopython=True)
def get_value_for_yesterday(variable, variable_0, Y_in, i_in, j_in, NYrs, DaysMonth):
    yesterday = variable_0
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if (Y == Y_in and i == i_in and j == j_in):
                    return yesterday
                else:
                    yesterday = variable[Y][i][j]

def get_value_for_yesterday_2(variable, variable_0, Y_in, i_in, j_in, DaysMonth):
    temp = variable
    key = random.randint(100000000000,999999999999)#use something that is hopefully unique so we can find it again
    temp[Y_in,i_in,j_in] = key
    temp = ymd_to_daily(temp,DaysMonth)
    today = where(temp==key)[0]
    if(len(today) != 1):
        raise AssertionError("this array has values equal to inf")
    if(today[0]-1 > 0):
        return temp[today[0]-1]
    else:#at the first index of the array
        return variable_0

# @jit(cache=True, nopython=True)
# def get_value_for_yesterday_yesterday(variable, variable_0, Y_in, i_in, j_in, NYrs, DaysMonth):
#     yesterday_yesterday = variable_0
#     yesterday = 0
#     for Y in range(NYrs):
#         for i in range(12):
#             for j in range(DaysMonth[Y][i]):
#                 if (Y == Y_in and i == i_in and j == j_in):
#                     return yesterday_yesterday
#                 else:
#                     yesterday_yesterday = yesterday
#                     yesterday = variable[Y][i][j]
#
#
# @jit(cache=True, nopython=True)
# def get_value_for_yesterday_yesterday_yesterday(variable, variable_0, Y_in, i_in, j_in, NYrs, DaysMonth):
#     yesterday_yesterday_yesterday = variable_0
#     yesterday_yesterday = 0
#     yesterday = 0
#     for Y in range(NYrs):
#         for i in range(12):
#             for j in range(DaysMonth[Y][i]):
#                 if (Y == Y_in and i == i_in and j == j_in):
#                     return yesterday_yesterday_yesterday
#                 else:
#                     yesterday_yesterday_yesterday = yesterday_yesterday
#                     yesterday_yesterday = yesterday
#                     yesterday = variable[Y][i][j]
