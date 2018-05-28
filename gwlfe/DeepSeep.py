import numpy as np
from numba import jit
from Timer import time_function
from Percolation import Percolation
from Percolation import Percolation_2
from Memoization import memoize
from numba.pycc import CC
from CompiledFunction import compiled


cc = CC('gwlfe_compiled')

@memoize
def DeepSeep(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
             ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef):
    result = np.zeros((NYrs, 12, 31))
    grflow = np.zeros((NYrs, 12, 31))
    satstor = np.zeros((NYrs, 12, 31))
    percolation = Percolation(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0,
                              Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap)
    satstor_carryover = SatStor_0
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                satstor[Y][i][j] = satstor_carryover
                grflow[Y][i][j] = RecessionCoef * satstor[Y][i][j]
                result[Y][i][j] = SeepCoef * satstor[Y][i][j]
                satstor[Y][i][j] = satstor[Y][i][j] + percolation[Y][i][j] - grflow[Y][i][j] - result[Y][i][j]
                if satstor[Y][i][j] < 0:
                    satstor[Y][i][j] = 0
                satstor_carryover = satstor[Y][i][j]
    return result


# --- LINE 36 ---
    #   NYrs = arg(0, name=NYrs)  :: int64
    #   SatStor_0 = arg(1, name=SatStor_0)  :: float64
    #   DaysMonth = arg(2, name=DaysMonth)  :: array(int64, 2d, C)
    #   RecessionCoef = arg(3, name=RecessionCoef)  :: float64
    #   SeepCoef = arg(4, name=SeepCoef)  :: float64
    #   percolation = arg(5, name=percolation)  :: array(float64, 3d, C)
    #   $0.1 = global(np: <module 'numpy' from '/Users/bs643/anaconda3/envs/gwlfeEnv/lib/python2.7/site-packages/numpy/__init__.pyc'>)  :: Module(<module 'numpy' from '/Users/bs643/anaconda3/envs/gwlfeEnv/lib/python2.7/site-packages/numpy/__init__.pyc'>)
    #   $0.2 = getattr(attr=zeros, value=$0.1)  :: Function(<built-in function zeros>)
    #   $const0.4 = const(int, 12)  :: int64
    #   $const0.5 = const(int, 31)  :: int64
    #   $0.6 = build_tuple(items=[Var(NYrs, /Users/bs643/Documents/ANS/gwlfe_develop/gwlf-e/gwlfe/DeepSeep.py (36)), Var($const0.4, /Users/bs643/Documents/ANS/gwlfe_develop/gwlf-e/gwlfe/DeepSeep.py (36)), Var($const0.5, /Users/bs643/Documents/ANS/gwlfe_develop/gwlf-e/gwlfe/DeepSeep.py (36))])  :: (int64 x 3)
    #   $0.7 = call $0.2($0.6, kws=[], args=[Var($0.6, /Users/bs643/Documents/ANS/gwlfe_develop/gwlf-e/gwlfe/DeepSeep.py (36))], func=$0.2, vararg=None)  :: ((int64 x 3),) -> array(float64, 3d, C)
    #   deepseep = $0.7  :: array(float64, 3d, C)

# @memoize
# @jit(cache=True, nopython=True)
@compiled
@cc.export('DeepSeep_inner', '(int64, float64, int64[:,::1], float64, float64, float64[:,:,::1])')
def DeepSeep_inner(NYrs, SatStor_0, DaysMonth, RecessionCoef, SeepCoef, percolation):
    deepseep = np.zeros((NYrs, 12, 31))
    grflow = np.zeros((NYrs, 12, 31))
    satstor = np.zeros((NYrs, 12, 31))
    satstor_carryover = SatStor_0
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                satstor[Y][i][j] = satstor_carryover
                grflow[Y][i][j] = RecessionCoef * satstor[Y][i][j]
                deepseep[Y][i][j] = SeepCoef * satstor[Y][i][j]
                satstor[Y][i][j] = satstor[Y][i][j] + percolation[Y][i][j] - grflow[Y][i][j] - deepseep[Y][i][j]
                if satstor[Y][i][j] < 0:
                    satstor[Y][i][j] = 0
                satstor_carryover = satstor[Y][i][j]
    return deepseep, grflow, satstor


# @memoize
def DeepSeep_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
               ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef):
    # cc.compile()
    percolation = Percolation_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow,
                                CNP_0,
                                Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap)

    temp =  DeepSeep_inner(NYrs, SatStor_0, DaysMonth, RecessionCoef, SeepCoef, percolation)[0]
    # print (DeepSeep_inner.inspect_types())
    return temp