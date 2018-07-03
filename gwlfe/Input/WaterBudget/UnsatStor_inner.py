from numba.pycc import CC
from numpy import zeros

cc = CC('UnsatStor_inner_compiled')


@cc.export('UnsatStor_inner', '(int64,int64[:,::1],float64,float64,float64[:,:,::1],float64[:,:,::1])')
def UnsatStor_inner(NYrs, DaysMonth, MaxWaterCap, UnsatStor_0, infiltration, DailyET):
    unsatstor = zeros((NYrs, 12, 31))
    unsatstor_carryover = UnsatStor_0
    et = zeros((NYrs, 12, 31))
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                unsatstor[Y][i][j] = unsatstor_carryover
                unsatstor[Y][i][j] = unsatstor[Y][i][j] + infiltration[Y][i][j]
                if DailyET[Y][i][j] >= unsatstor[Y][i][j]:
                    et[Y][i][j] = unsatstor[Y][i][j]
                    unsatstor[Y][i][j] = 0
                else:
                    et[Y][i][j] = DailyET[Y][i][j]
                    unsatstor[Y][i][j] = unsatstor[Y][i][j] - DailyET[Y][i][j]
                if unsatstor[Y][i][j] > MaxWaterCap:
                    unsatstor[Y][i][j] = MaxWaterCap
                else:
                    pass
                unsatstor_carryover = unsatstor[Y][i][j]
    return unsatstor, et, unsatstor_carryover
