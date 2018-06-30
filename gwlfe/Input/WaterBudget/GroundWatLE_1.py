from numpy import maximum
from numpy import zeros

from gwlfe.Input.LandUse.Ag.TileDrainGW import TileDrainGW
from gwlfe.Input.LandUse.Ag.TileDrainGW import TileDrainGW_f
from gwlfe.Input.WaterBudget.GroundWatLE import GroundWatLE
from gwlfe.Input.WaterBudget.GroundWatLE import GroundWatLE_f
from gwlfe.Memoization import memoize


@memoize
def GroundWatLE_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                  ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef,
                  Landuse, TileDrainDensity):
    result = zeros((NYrs, 12))
    tiledraingw = TileDrainGW(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                              CNP_0,
                              Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                              RecessionCoef,
                              SeepCoef, Landuse, TileDrainDensity)
    grounwatle_1 = GroundWatLE(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                               CNP_0, Imper,
                               ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef,
                               SeepCoef)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = grounwatle_1[Y][i] - tiledraingw[Y][i]
        if result[Y][i] < 0:
            result[Y][i] = 0
    return result


@memoize
def GroundWatLE_1_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                    ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef,
                    Landuse, TileDrainDensity):
    result = zeros((NYrs, 12))
    tiledraingw = TileDrainGW_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                                CNP_0,
                                Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                                RecessionCoef,
                                SeepCoef, Landuse, TileDrainDensity)
    grounwatle = GroundWatLE_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                               Grow_0,
                               CNP_0, Imper,
                               ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                               RecessionCoef,
                               SeepCoef)
    result = grounwatle - tiledraingw
    return maximum(result, 0)
