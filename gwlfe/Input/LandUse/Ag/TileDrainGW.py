from numpy import zeros

from gwlfe.Input.LandUse.Ag.GwAgLE import GwAgLE
from gwlfe.Input.LandUse.Ag.GwAgLE import GwAgLE_f
from gwlfe.Memoization import memoize


@memoize
def TileDrainGW(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef,
                Landuse, TileDrainDensity):
    result = zeros((NYrs, 12))
    gwagle = GwAgLE(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                    ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef,
                    Landuse)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = (result[Y][i] + [gwagle[Y][i] * TileDrainDensity])
    return result


@memoize
def TileDrainGW_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                  ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef,
                  Landuse, TileDrainDensity):
    if (TileDrainDensity > 0):
        gwagle = GwAgLE_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                          Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef,
                          SeepCoef, Landuse)
        return gwagle * TileDrainDensity
    else:
        return zeros((NYrs, 12))
