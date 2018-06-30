from numpy import zeros

from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Runoff.RurQRunoff import RurQRunoff
from gwlfe.MultiUse_Fxns.Runoff.RurQRunoff import RurQRunoff_f
from gwlfe.Output.Loading.NConc import NConc
from gwlfe.Output.Loading.NConc import NConc_f


@memoize
def nRunoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0, Area, NitrConc,
            ManNitr, ManuredAreas, FirstManureMonth, LastManureMonth, FirstManureMonth2, LastManureMonth2):
    result = zeros((NYrs, 12, 10))
    rur_q_runoff = RurQRunoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0)
    n_conc = NConc(NRur, NUrb, NitrConc, ManNitr, ManuredAreas, FirstManureMonth, LastManureMonth, FirstManureMonth2,
                   LastManureMonth2)
    for Y in range(NYrs):
        for i in range(12):
            for l in range(NRur):
                result[Y][i][l] = 0.1 * n_conc[i][l] * rur_q_runoff[Y][l][i] * Area[l]
    # += changed to =
    return result


@memoize
def nRunoff_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0, Area, NitrConc,
              ManNitr, ManuredAreas, FirstManureMonth, LastManureMonth, FirstManureMonth2, LastManureMonth2):
    n_conc = NConc_f(NRur, NUrb, NitrConc, ManNitr, ManuredAreas, FirstManureMonth, LastManureMonth, FirstManureMonth2,
                     LastManureMonth2)[:, :NRur]

    return 0.1 * n_conc * RurQRunoff_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN,
                                       Grow_0) * Area[:NRur]
