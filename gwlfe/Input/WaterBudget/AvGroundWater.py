from numpy import sum
from numpy import zeros

from gwlfe.Input.WaterBudget.GroundWatLE_1 import GroundWatLE_1
from gwlfe.Input.WaterBudget.GroundWatLE_1 import GroundWatLE_1_f
from gwlfe.Memoization import memoize


def AvGroundWater(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0,
                  AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap,
                  SatStor_0, RecessionCoef, SeepCoef, Landuse, TileDrainDensity):
    result = zeros(12)
    ground_wat_le = GroundWatLE_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                                  CNP_0, Imper,
                                  ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                                  RecessionCoef, SeepCoef,
                                  Landuse, TileDrainDensity)
    for Y in range(NYrs):
        for i in range(12):
            result[i] += ground_wat_le[Y][i] / NYrs
    return result


@memoize
def AvGroundWater_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0,
                    AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap,
                    SatStor_0, RecessionCoef, SeepCoef, Landuse, TileDrainDensity):
    return sum(GroundWatLE_1_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0,
                               AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs,
                               MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef, Landuse, TileDrainDensity),
               axis=0) / NYrs
