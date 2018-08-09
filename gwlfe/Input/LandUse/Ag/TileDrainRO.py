from numpy import zeros

from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Runoff.AgRunoff import AgRunoff
from gwlfe.MultiUse_Fxns.Runoff.AgRunoff import AgRunoff_f


@memoize
def TileDrainRO(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, AntMoist_0, NUrb, Grow_0, Landuse, Area,
                TileDrainDensity):
    result = zeros((NYrs, 12))
    ag_runoff = AgRunoff(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, AntMoist_0, NUrb, Grow_0, Landuse, Area)
    for Y in range(NYrs):
        for i in range(12):
            # CALCULATE THE SURFACE RUNOFF PORTION OF TILE DRAINAGE
            result[Y][i] = ag_runoff[Y][i] * TileDrainDensity
    return result


@memoize
def TileDrainRO_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, AntMoist_0, NUrb, Grow_0, Landuse, Area,
                  TileDrainDensity):
    return AgRunoff_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, AntMoist_0, NUrb, Grow_0, Landuse,
                      Area) * TileDrainDensity
