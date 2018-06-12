import numpy as np
# from Timer import time_function
from Memoization import memoize
from NLU import NLU
from LuLoad import LuLoad
from LuLoad import LuLoad_2

# #TODO: this variable is not used
# def UrbSedLoad(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0,
#                      AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil,
#                      Nqual, LoadRateImp, LoadRatePerv, Storm, UrbBMPRed,
#                      FilterWidth, PctStrmBuf):
#     result = np.zeros((16, 12))
#     nlu = NLU(NRur, NUrb)
#     lu_load = LuLoad(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0,
#              AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil,
#              Nqual, LoadRateImp, LoadRatePerv, Storm, UrbBMPRed,
#              FilterWidth, PctStrmBuf)
#     for Y in range(NYrs):
#         for i in range(12):
#             # Add in the urban calucation for sediment
#             for l in range(NRur, nlu):
#                 result[l][i] += lu_load[Y][l][2]
#     return result
#
# def UrbSedLoad_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0,
#            AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil,
#            Nqual, LoadRateImp, LoadRatePerv, Storm, UrbBMPRed,
#            FilterWidth, PctStrmBuf):
#     return np.reshape(np.repeat(np.sum(LuLoad_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0,
#            AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil,
#            Nqual, LoadRateImp, LoadRatePerv, Storm, UrbBMPRed,
#            FilterWidth, PctStrmBuf)[:,:,2],axis=0),repeats=12),(-1,12))
