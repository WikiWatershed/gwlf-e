from numba import jit


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
