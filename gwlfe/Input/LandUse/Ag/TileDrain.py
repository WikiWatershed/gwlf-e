from numpy import zeros

from gwlfe.Input.LandUse.Ag.TileDrainGW import TileDrainGW
from gwlfe.Input.LandUse.Ag.TileDrainGW import TileDrainGW_f
from gwlfe.Input.LandUse.Ag.TileDrainRO import TileDrainRO
from gwlfe.Input.LandUse.Ag.TileDrainRO import TileDrainRO_f
from gwlfe.Memoization import memoize


def TileDrain(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
              ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef, Landuse,
              TileDrainDensity):
    result = zeros((NYrs, 12))
    tiledrainro = TileDrainRO(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, AntMoist_0, NUrb, Grow_0, Landuse,
                              Area,
                              TileDrainDensity)
    tiledraingw = TileDrainGW(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                              CNP_0,
                              Imper,
                              ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef,
                              SeepCoef, Landuse, TileDrainDensity)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = (result[Y][i] + tiledrainro[Y][i] + tiledraingw[Y][i])
    return result


@memoize
def TileDrain_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef,
                Landuse, TileDrainDensity):
    tiledrainro = TileDrainRO_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, AntMoist_0, NUrb, Grow_0, Landuse,
                                Area,
                                TileDrainDensity)
    tiledraingw = TileDrainGW_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                                CNP_0,
                                Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                                RecessionCoef, SeepCoef, Landuse, TileDrainDensity)
    return tiledrainro + tiledraingw
