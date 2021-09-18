from numpy import zeros

from gwlfe.Input.WaterBudget.ET import DailyET_f
from gwlfe.Input.WaterBudget.Infiltration import Infiltration
from gwlfe.Input.WaterBudget.Infiltration import Infiltration_f
from gwlfe.Memoization import memoize

try:
    from .Percolation_inner_compiled import Percolation_inner
except ImportError:
    print("Unable to import compiled Percolation_inner, using slower version")
    from gwlfe.Input.WaterBudget.Percolation_inner import Percolation_inner


@memoize
def Percolation(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap):
    result = zeros((NYrs, 12, 31))
    percolation = zeros((NYrs, 12, 31))
    infiltration = Infiltration(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                                CNP_0, Imper,
                                ISRR, ISRA, CN)
    unsatstor_carryover = UnsatStor_0
    et = DailyET_f(Temp, KV, PcntET, DayHrs)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                result[Y][i][j] = unsatstor_carryover
                result[Y][i][j] = result[Y][i][j] + infiltration[Y][i][j]
                if et[Y][i][j] >= result[Y][i][j]:
                    result[Y][i][j] = 0
                else:
                    result[Y][i][j] = result[Y][i][j] - et[Y][i][j]
                if result[Y][i][j] > MaxWaterCap:
                    percolation[Y][i][j] = result[Y][i][j] - MaxWaterCap
                    result[Y][i][j] = MaxWaterCap
                else:
                    pass
                unsatstor_carryover = result[Y][i][j]
    return percolation


def Percolation_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                  ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap):
    infiltration = Infiltration_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                                  CNP_0, Imper, ISRR, ISRA, CN)

    et = DailyET_f(Temp, KV, PcntET, DayHrs)
    return Percolation_inner(NYrs, UnsatStor_0, DaysMonth, MaxWaterCap, infiltration, et)
