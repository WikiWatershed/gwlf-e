from numba.pycc import CC
import numpy as np

cc = CC('UnsatStor_inner_compiled')


@cc.export('UnsatStor_inner', '(int64,int32[:,::1],float64,float64,float64[:,:,::1],float64[:,:,::1])')
def UnsatStor_inner(NYrs, DaysMonth, MaxWaterCap, UnsatStor_0, infiltration, et):
    result = np.zeros((NYrs, 12, 31))
    unsatstor_carryover = UnsatStor_0
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
                    result[Y][i][j] = MaxWaterCap
                else:
                    pass
                unsatstor_carryover = result[Y][i][j]
    return result, et
