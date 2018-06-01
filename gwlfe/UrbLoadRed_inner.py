from numba import jit
import numpy as np

@jit(cache=True, nopython= True)
def UrbLoadRed_inner(NYrs, DaysMonth, Temp,  NRur, Nqual, Storm, UrbBMPRed, water, adjurbanqtotal, nlu):
    result = np.zeros((NYrs, 12, 31, 16, Nqual))
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    # result[Y][i][j][l][q] = 0
                    if adjurbanqtotal[Y][i][j] > 0.001:
                        for l in range(NRur, nlu):
                            for q in range(Nqual):
                                result[Y][i][j][l][q] = (water[Y][i][j] / Storm) * UrbBMPRed[l][q]
                                if water[Y][i][j] > Storm:
                                    result[Y][i][j][l][q] = UrbBMPRed[l][q]
                else:
                    pass
    return result