import math

from numba.pycc import CC
from numpy import exp
from numpy import zeros

cc = CC('WashPerv_inner_compiled')


@cc.export('WashPerv_inner',
           '(int64, int64[:,::1], float64[:,:,::1], int64, int64, float64[:,:,::1], float64[:,:,:,::1])')
def WashPerv_inner(NYrs, DaysMonth, Temp, NRur, nlu, water, qrunp):
    washperv = zeros((NYrs, 12, 31, 16))
    pervaccum = zeros(16)  # TODO: why is this here?
    carryover = zeros(16)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                for l in range(nlu):
                    pervaccum[l] = carryover[l]
                    pervaccum[l] = (pervaccum[l] * exp(-0.12) + (1 / 0.12) * (1 - exp(-0.12)))
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if water[Y][i][j] < 0.05:
                        pass
                    else:
                        for l in range(NRur, nlu):
                            washperv[Y][i][j][l] = (1 - math.exp(-1.81 * qrunp[Y][i][j][l])) * pervaccum[l]
                            pervaccum[l] -= washperv[Y][i][j][l]
                else:
                    pass
                for l in range(nlu):
                    carryover[l] = pervaccum[l]
    return washperv
