from numpy import sum
from numpy import zeros

# from Timer import time_function
from gwlfe.Input.WaterBudget.GrFlow import GrFlow
from gwlfe.Input.WaterBudget.GrFlow import GrFlow_f
from gwlfe.Memoization import memoize


@memoize
def GroundWatLE(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef):
    result = zeros((NYrs, 12))
    grflow = GrFlow(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                    ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                result[Y][i] = result[Y][i] + grflow[Y][i][j]
    return result


@memoize
def GroundWatLE_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                  ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef):
    grflow = GrFlow_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                      Imper,
                      ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef)
    return sum(grflow, axis=2)

# THIS IS A FUNCTION THAT FULLY SATISFIES GroundWatLE and matches the original model output. NOTHING IS SEPARATED YET
# def GroundWatLE_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
#            ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef, Landuse, TileDrainDensity):
#     result = np.zeros((NYrs, 12))
#     areatotal = AreaTotal(NRur, NUrb, Area) #4129.0
#     agareatotal = AgAreaTotal(NRur, Landuse, Area) # 2499.0
#     grflow = GrFlow(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
#            ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef)
#     gwagle = np.zeros((NYrs, 12))
#     tiledraingw = np.zeros((NYrs, 12))
#     for Y in range(NYrs):
#         for i in range(12):
#             for j in range(DaysMonth[Y][i]):
#                 result[Y][i] = result[Y][i] + grflow[Y][i][j]
#             if areatotal > 0:
#                 gwagle[Y][i] = (gwagle[Y][i] + (result[Y][i] * (agareatotal / areatotal)))
#             tiledraingw[Y][i] = (tiledraingw[Y][i] + [gwagle[Y][i] * TileDrainDensity])
#             result[Y][i] = result[Y][i] - tiledraingw[Y][i]
#             if result[Y][i] < 0:
#                 result[Y][i] = 0
#     #return result
#     pass
