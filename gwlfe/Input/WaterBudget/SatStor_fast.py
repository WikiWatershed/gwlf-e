from numpy import zeros

from gwlfe.Memoization import memoize
# from Timer import time_function
from gwlfe.Input.WaterBudget.Percolation import Percolation
from gwlfe.Input.WaterBudget.Percolation import Percolation_2
import numpy as np
try:
    from DeepSeep_inner_compiled import DeepSeep_inner
except ImportError:
    print("Unable to import compiled DeepSeep_inner, using slower version")
    from gwlfe.Input.WaterBudget.DeepSeep_inner import DeepSeep_inner




def SatStor_accumulate(DaysMonth, NYrs, RecessionCoef, SeepCoef, percolation, SatStor_0=0):
    result = zeros((NYrs, 12, 31))
    grflow = zeros((NYrs, 12, 31))
    deepseep = zeros((NYrs, 12, 31))

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
def SatStor(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
            ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef):
    percolation = Percolation(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                              Imper,
                              ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap)
    return SatStor_accumulate(DaysMonth, NYrs, RecessionCoef, SatStor_0, SeepCoef, percolation)


def SatStor_accumulate_fast(DaysMonth, NYrs, RecessionCoef, SeepCoef, percolation, SatStor_0=0,):
    mult= RecessionCoef+SeepCoef
    # day_mask=np.zeros_like(percolation, dtype=np.bool)
    # for YY in range(int(NYrs)):
    #     for ii in range(12):
    #         ndays = int(DaysMonth[YY,ii])
    #         day_mask[YY,ii, 0:ndays]=True
    # percolation=percolation[np.where(day_mask)]
    percolation= percolation.flatten()
    result= np.zeros_like(percolation)
    result[0]=SatStor_0
    it = np.nditer([percolation, result], flags=[ 'external_loop'],
                   op_flags = [['readonly'], ['readwrite']],
                   )
    it.operands[1][...] = 0
    for per, st in it:
        st[...] = np.clip(st + per - (mult * st), 0, np.inf)
    return it.operands[1]


def SatStor_accumulate_test():
    sz=(300,12,31)
    DaysMonth=np.zeros((sz[0], sz[1]), dtype='int')
    DaysMonth[:,:]=31
    RecessionCoef, SeepCoef=(.3,.9)
    percolation = np.random.normal(size=sz)
    res1=SatStor_accumulate(DaysMonth, 300, RecessionCoef, SeepCoef, percolation, SatStor_0=0 ).flatten()
    # res2=SatStor_accumulate_old(DaysMonth, 300, RecessionCoef, SeepCoef, percolation, SatStor_0=0 ).flatten()
    # print(res2.shape)
    # print(res2-res1)

@memoize
def SatStor_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
              ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef):
    percolation = Percolation_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                                CNP_0,
                                Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap)
    return DeepSeep_inner(NYrs, SatStor_0, DaysMonth, RecessionCoef, SeepCoef, percolation)[2]
