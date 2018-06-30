from numpy import repeat
from numpy import tile
from numpy import where
from numpy import zeros

from gwlfe.Input.LandUse.NLU import NLU
from gwlfe.Input.WaterBudget.Water import Water, Water_f
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Runoff.CNI import CNI, CNI_f
from gwlfe.MultiUse_Fxns.Runoff.CNumImperv import CNumImperv, CNumImperv_f


@memoize
def CNumImpervReten(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, NRur, NUrb, CNI_0,
                    Grow_0):  # TODO: this is exactly the same as perv and retention
    cni = CNI(NRur, NUrb, CNI_0)
    c_num_imperv = CNumImperv(NYrs, NRur, NUrb, DaysMonth, InitSnow_0, Temp, Prec, CNI_0, Grow_0, AntMoist_0)
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
                            if cni[1][l] > 0:
                                result[Y][i][j][l] = 2540 / c_num_imperv[Y][i][j][l] - 25.4
                                if result[Y][i][j][l] < 0:
                                    result[Y][i][j][l] = 0
    return result


def CNumImpervReten_f(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, NRur, NUrb, CNI_0, Grow_0):
    cni = CNI_f(NRur, NUrb, CNI_0)
    cni_1 = tile(cni[1][None, None, None, :], (NYrs, 12, 31, 1))
    c_num_imperv = CNumImperv_f(NYrs, NRur, NUrb, DaysMonth, InitSnow_0, Temp, Prec, CNI_0, Grow_0, AntMoist_0)
    nlu = NLU(NRur, NUrb)
    water = repeat(Water_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec)[:, :, :, None], nlu, axis=3)
    result = zeros((NYrs, 12, 31, nlu))
    TempE = repeat(Temp[:, :, :, None], nlu, axis=3)
    result[where((TempE > 0) & (water >= 0.05) & (cni_1 > 0))] = 2540 / c_num_imperv[
        where((TempE > 0) & (water >= 0.05) & (cni_1 > 0))] - 25.4
    result[where(result < 0)] = 0
    return result
