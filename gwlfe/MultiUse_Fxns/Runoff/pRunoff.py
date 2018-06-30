from numpy import zeros

from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Runoff.RurQRunoff import RurQRunoff
from gwlfe.MultiUse_Fxns.Runoff.RurQRunoff import RurQRunoff_f
from gwlfe.Output.Loading.PConc import PConc
from gwlfe.Output.Loading.PConc import PConc_f


@memoize
def pRunoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0, Area, PhosConc, ManuredAreas,
            FirstManureMonth, LastManureMonth, ManPhos, FirstManureMonth2,
            LastManureMonth2):
    result = zeros((NYrs, 12, 10))
    rur_q_runoff = RurQRunoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0)
    p_conc = PConc(NRur, NUrb, PhosConc, ManPhos, ManuredAreas, FirstManureMonth, LastManureMonth, FirstManureMonth2,
                   LastManureMonth2)
    for Y in range(NYrs):
        for i in range(12):
            for l in range(NRur):
                # += changed to =
                result[Y][i][l] = 0.1 * p_conc[i][l] * rur_q_runoff[Y][l][i] * Area[l]
    return result


@memoize
def pRunoff_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0, Area, PhosConc, ManuredAreas,
              FirstManureMonth, LastManureMonth, ManPhos, FirstManureMonth2, LastManureMonth2):
    p_conc = PConc_f(NRur, NUrb, PhosConc, ManPhos, ManuredAreas, FirstManureMonth, LastManureMonth, FirstManureMonth2,
                     LastManureMonth2)[:, :NRur]
    rur_q_runoff = RurQRunoff_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0)
    return 0.1 * p_conc * rur_q_runoff * Area[:NRur]
