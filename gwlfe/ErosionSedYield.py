from BSed import BSed
from Memoization import memoize
from RurEros import RurEros
from SedDelivRatio import SedDelivRatio
from SedTrans import SedTrans
from StreamBankEros_1 import StreamBankEros_1
from Water import Water


@memoize
def ErosionSedYield(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area, SedDelivRatio_0,
                    NUrb, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN,
                    UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef,
                    Landuse, TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
                    NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF, AvSlope, SedAAdjust, StreamLength,
                    n42b, n46c, n85d, AgLength, n42, n45, n85, UrbBankStab):
    erosion = zeros((NYrs, 12))
    sedyield = zeros((NYrs, 12))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    rureros = RurEros(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area)
    bsed = BSed(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN)
    seddelivratio = SedDelivRatio(SedDelivRatio_0)
    sedtrans = SedTrans(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                        Imper,
                        ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN)
    streambankeros_2 = StreamBankEros_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                                        Grow_0, CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs,
                                        MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b,
                                        Landuse, TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal
                                        , NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF, AvSlope,
                                        SedAAdjust, StreamLength, n42b, n46c, n85d, AgLength, n42, n45, n85,
                                        UrbBankStab)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                for l in range(NRur):
                    if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                        erosion[Y][i] = erosion[Y][i] + rureros[Y][i][j][l]
                    else:
                        pass
            for m in range(i + 1):
                if bsed[Y][m] > 0:
                    sedyield[Y][i] += erosion[Y][m] / bsed[Y][m]
            sedyield[Y][i] = seddelivratio * sedtrans[Y][i] * sedyield[Y][i]
            # TODO These are now used to calculate: SedYieldTotal, ErosionTotal, TotalNitr, and TotalPhos
        for i in range(12):
            sedyield[Y][i] += streambankeros_2[Y][i] / 1000
            if seddelivratio > 0 and erosion[Y][i] < sedyield[Y][i]:
                erosion[Y][i] = sedyield[Y][i] / seddelivratio
            # TODO Now calculated is: AvSedYield, ErosSum, and AvErosion
    pass


def ErosionSedYield_2():
    pass
