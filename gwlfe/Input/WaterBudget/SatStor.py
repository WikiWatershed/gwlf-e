from numpy import zeros

from gwlfe.Input.WaterBudget.Percolation import Percolation
from gwlfe.Input.WaterBudget.Percolation import Percolation_f
from gwlfe.Memoization import memoize

try:
    from .DeepSeep_inner_compiled import DeepSeep_inner
except ImportError:
    print("Unable to import compiled DeepSeep_inner, using slower version")
    from gwlfe.Input.WaterBudget.DeepSeep_inner import DeepSeep_inner


@memoize
def SatStor(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
            ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef):
    result = zeros((NYrs, 12, 31))
    grflow = zeros((NYrs, 12, 31))
    deepseep = zeros((NYrs, 12, 31))
    percolation = Percolation(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                              CNP_0,
                              Imper,
                              ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap)
    satstor_carryover = SatStor_0
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                result[Y][i][j] = satstor_carryover
                grflow[Y][i][j] = RecessionCoef * result[Y][i][j]
                deepseep[Y][i][j] = SeepCoef * result[Y][i][j]
                result[Y][i][j] = result[Y][i][j] + percolation[Y][i][j] - grflow[Y][i][j] - deepseep[Y][i][j]
                if result[Y][i][j] < 0:
                    result[Y][i][j] = 0
                satstor_carryover = result[Y][i][j]
    return result


@memoize
def SatStor_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
              ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef):
    percolation = Percolation_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                                CNP_0,
                                Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap)
    return DeepSeep_inner(NYrs, SatStor_0, DaysMonth, RecessionCoef, SeepCoef, percolation)[2]
