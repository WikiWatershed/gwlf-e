from numpy import repeat
from numpy import tile
from numpy import where
from numpy import zeros

from gwlfe.Input.LandUse.NLU import NLU
from gwlfe.Input.WaterBudget.Water import Water, Water_f
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Runoff.CNP import CNP, CNP_f
from gwlfe.MultiUse_Fxns.Runoff.CNumPerv import CNumPerv, CNumPerv_f


@memoize
def CNumPervReten(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, NRur, NUrb, CNP_0, Grow_0):
    cnp = CNP(NRur, NUrb, CNP_0)
    c_num_perv = CNumPerv(NYrs, DaysMonth, Temp, NRur, NUrb, CNP_0, InitSnow_0, Prec, Grow_0, AntMoist_0)
    nlu = NLU(NRur, NUrb)
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    result = zeros((NYrs, 12, 31, nlu))
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:  # missing
                    if water[Y][i][j] < 0.05:  # missing
                        pass
                    else:
                        for l in range(NRur, nlu):
                            if cnp[1][l] > 0:
                                result[Y][i][j][l] = 2540 / c_num_perv[Y][i][j][l] - 25.4
                                if result[Y][i][j][l] < 0:
                                    result[Y][i][j][l] = 0
    return result


def CNumPervReten_f(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, NRur, NUrb, CNP_0, Grow_0):
    nlu = NLU(NRur, NUrb)
    result = zeros((NYrs, 12, 31, nlu))
    c_num_perv = CNumPerv_f(NYrs, DaysMonth, Temp, NRur, NUrb, CNP_0, InitSnow_0, Prec, Grow_0, AntMoist_0)
    cnp = CNP_f(NRur, NUrb, CNP_0)
    cnp_1 = tile(cnp[1][None, None, None, :], (NYrs, 12, 31, 1))
    water = repeat(Water_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec)[:, :, :, None], nlu, axis=3)
    Temp = repeat(Temp[:, :, :, None], nlu, axis=3)
    result[where((Temp > 0) & (water >= 0.05) & (cnp_1 > 0))] = 2540 / c_num_perv[
        where((Temp > 0) & (water >= 0.05) & (cnp_1 > 0))] - 25.4
    result[where(result < 0)] = 0
    return result
