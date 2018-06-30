from numpy import hstack
from numpy import sum
from numpy import zeros

from gwlfe.Input.LandUse.NLU import NLU
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Runoff.RurQRunoff import RurQRunoff
from gwlfe.MultiUse_Fxns.Runoff.RurQRunoff import RurQRunoff_f
from gwlfe.MultiUse_Fxns.Runoff.UrbQRunoff import UrbQRunoff
from gwlfe.MultiUse_Fxns.Runoff.UrbQRunoff import UrbQRunoff_f


def LuRunoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, CNI_0, CNP_0,
             AntMoist_0, Grow_0, Imper, ISRR, ISRA, CN):
    result = zeros((NYrs, 16))
    nlu = NLU(NRur, NUrb)
    urb_q_runoff = UrbQRunoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, CNI_0, CNP_0,
                              AntMoist_0, Grow_0, Imper, ISRR, ISRA)
    rur_q_runoff = RurQRunoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0)
    for Y in range(NYrs):
        for i in range(12):
            # Calculate landuse runoff for rural areas
            for l in range(NRur):
                result[Y][l] += rur_q_runoff[Y][l][i]
        for i in range(12):
            # Calculate landuse runoff for urban areas
            for l in range(NRur, nlu):
                result[Y][l] += urb_q_runoff[Y][l][i]
    return result


@memoize
def LuRunoff_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, CNI_0, CNP_0,
               AntMoist_0, Grow_0, Imper, ISRR, ISRA, CN):
    return hstack(
        (sum(RurQRunoff_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0), axis=1),
         sum(UrbQRunoff_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, CNI_0, CNP_0,
                          AntMoist_0, Grow_0, Imper, ISRR, ISRA), axis=1),
         ))
