from numba import jit
import numpy as np


def ymd_to_daily(ymd_array, leap_year=False):
    if (leap_year == False):
        mask = np.r_[0:31, 32:59, 62:93, 94:]
    return np.ravel(ymd_array)[0:31]


@jit(cache=True, nopython=True)
def get_value_for_yesterday(variable, variable_0, Y_in, i_in, j_in, NYrs, DaysMonth):
    yesterday = variable_0
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if (Y == Y_in and i == i_in and j == j_in):
                    return yesterday
                else:
                    yesterday = variable[Y][i][j]


@jit(cache=True, nopython=True)
def get_value_for_yesterday_yesterday(variable, variable_0, Y_in, i_in, j_in, NYrs, DaysMonth):
    yesterday_yesterday = variable_0
    yesterday = 0
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if (Y == Y_in and i == i_in and j == j_in):
                    return yesterday_yesterday
                else:
                    yesterday_yesterday = yesterday
                    yesterday = variable[Y][i][j]


@jit(cache=True, nopython=True)
def get_value_for_yesterday_yesterday_yesterday(variable, variable_0, Y_in, i_in, j_in, NYrs, DaysMonth):
    yesterday_yesterday_yesterday = variable_0
    yesterday_yesterday = 0
    yesterday = 0
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if (Y == Y_in and i == i_in and j == j_in):
                    return yesterday_yesterday_yesterday
                else:
                    yesterday_yesterday_yesterday = yesterday_yesterday
                    yesterday_yesterday = yesterday
                    yesterday = variable[Y][i][j]
