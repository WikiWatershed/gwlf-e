import numpy as np
from Timer import time_function
import json

# Grazing animal losses

def GRAppManN(GRPctManApp, InitGrN):
    result = np.zeros((12,))
    for i in range(12):
        result[i] = GRPctManApp[i] * InitGrN
    return result


def GRAppManN_2(GRPctManApp, InitGrN):
    return GRPctManApp * InitGrN


def GrazingN(PctGrazing, InitGrN):
    result = np.zeros((12,))
    for i in range(12):
        result[i] = PctGrazing[i] * (InitGrN / 12)
    return result


def GrazingN_2(PctGrazing, InitGrN):
    return PctGrazing * (InitGrN / 12)

def GRAccManAppN(InitGrN, GRPctManApp, GrazingN):
    result = np.zeros((12,))
    for i in range(12):
        result[i] = (result[i] + (InitGrN / 12)
                     - (GRPctManApp[i] * InitGrN) - GrazingN[i])
        if result[i] < 0:
            result[i] = 0
    return result

def GRAccManAppN_2(InitGrN, GRPctManApp, GrazingN):
    result = (np.repeat(InitGrN/12,12) ) - (GRPctManApp * np.repeat(InitGrN,12)) - GrazingN
    result = np.maximum(result,0)
    return result


def GRInitBarnN(GRAppManN, InitGrN, GRPctManApp, GrazingN):
    result = np.zeros((12,))
    grAccManAppN = GRAccManAppN(InitGrN, GRPctManApp, GrazingN)
    for i in range(12):
        result[i] = grAccManAppN[i] - GRAppManN[i]
    return result


def GRInitBarnN_2(GRAppManN, InitGrN, GRPctManApp, GrazingN):
    result = GRAccManAppN_2(InitGrN, GRPctManApp, GrazingN) - GRAppManN
    return result


def GRLostManN(NYrs, GRAppManN, GRAppNRate, LossFactAdj, GRPctSoilIncRate):
    result = np.zeros((NYrs, 12))
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = (GRAppManN[i] * GRAppNRate[i] * LossFactAdj[Y][i] * (1 - GRPctSoilIncRate[i]))
            if result[Y][i] > GRAppManN[i]:
                result[Y][i] = GRAppManN[i]
            if result[Y][i] < 0:
                result[Y][i] = 0
    return result


def GRLostManN_2(NYrs, GRAppManN, GRAppNRate, LossFactAdj, GRPctSoilIncRate):
    result = (np.tile( GRAppManN,NYrs) * np.tile( GRAppNRate, NYrs) * np.ndarray.flatten(LossFactAdj) * np.tile(( 1 - GRPctSoilIncRate),NYrs ))
    result = np.minimum(result, np.tile( GRAppManN, NYrs ) )
    result = np.maximum(result,0)
    return np.reshape(result,(NYrs,12))


def GRLostBarnN(NYrs, GRInitBarnN, GRBarnNRate, LossFactAdj, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN):
    result = np.zeros((NYrs, 12))
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = (GRInitBarnN[i] * GRBarnNRate[i] * LossFactAdj[Y][i]
                            - GRInitBarnN[i] * GRBarnNRate[i] * LossFactAdj[Y][i] * AWMSGrPct * GrAWMSCoeffN
                            + GRInitBarnN[i] * GRBarnNRate[i] * LossFactAdj[Y][i] * RunContPct * RunConCoeffN)
            if result[Y][i] > GRInitBarnN[i]:
                result[Y][i] = GRInitBarnN[i]
            if result[Y][i] < 0:
                result[Y][i] = 0
    return result


def GRLostBarnN_2(NYrs, GRInitBarnN, GRBarnNRate, LossFactAdj, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN):
    result = ( np.tile(GRInitBarnN, NYrs) * np.tile(GRBarnNRate,NYrs) * np.ndarray.flatten(LossFactAdj) * (1 - (AWMSGrPct * GrAWMSCoeffN) + (RunContPct * RunContPct)  ) )
    result = np.minimum(result, np.tile( GRInitBarnN, NYrs ) )
    result = np.maximum(result,0)
    return np.reshape(result,(NYrs,12))


def GRLossN(NYrs, GrazingN, GRStreamN, GrazingNRate, LossFactAdj):
    result = np.zeros((NYrs, 12))
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = ((GrazingN[i] - GRStreamN[i]) * GrazingNRate[i] * LossFactAdj[Y][i])
            if result[Y][i] > (GrazingN[i] - GRStreamN[i]):
                result[Y][i] = (GrazingN[i] - GRStreamN[i])
            if result[Y][i] < 0:
                result[Y][i] = 0
    return result


def GRLossN_2(NYrs, GrazingN, GRStreamN, GrazingNRate, LossFactAdj):
    result = ( np.tile( ( (GrazingN - GRStreamN) * GrazingNRate ), NYrs ) * np.ndarray.flatten(LossFactAdj))
    result = np.minimum(result, np.tile( (GrazingN-GRStreamN),NYrs))
    result = np.maximum(result, 0)
    return np.reshape(result,(NYrs,12))




# Non-grazing animal losses
def NGLostBarnN(NYrs, NGInitBarnN, NGBarnNRate, LossFactAdj, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN):
    result = np.zeros((NYrs, 12))
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = (NGInitBarnN[i] * NGBarnNRate[i] * LossFactAdj[Y][i]
                            - NGInitBarnN[i] * NGBarnNRate[i] * LossFactAdj[Y][i] * AWMSNgPct * NgAWMSCoeffN
                            + NGInitBarnN[i] * NGBarnNRate[i] * LossFactAdj[Y][i] * RunContPct * RunConCoeffN)
            if result[Y][i] > NGInitBarnN[i]:
                result[Y][i] = NGInitBarnN[i]
            if result[Y][i] < 0:
                result[Y][i] = 0
    return result


def NGLostBarnN_2(NYrs, NGInitBarnN, NGBarnNRate, LossFactAdj, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN):
    result = ( np.tile(NGInitBarnN, NYrs) * np.tile(NGBarnNRate,NYrs) * np.ndarray.flatten(LossFactAdj) * (1 - (AWMSNgPct * NgAWMSCoeffN) + (RunContPct * RunConCoeffN)  ) )
    result = np.minimum(result, np.tile( NGInitBarnN, NYrs ) )
    result = np.maximum(result,0)
    return np.reshape(result,(NYrs,12))


def NGLostManN(NYrs, NGAppManN, NGAppNRate, LossFactAdj, NGPctSoilIncRate):
    # Non-grazing animal losses
    result = np.zeros((NYrs, 12))
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = (NGAppManN[i] * NGAppNRate[i] * LossFactAdj[Y][i]
                            * (1 - NGPctSoilIncRate[i]))
            if result[Y][i] > NGAppManN[i]:
                result[Y][i] = NGAppManN[i]
            if result[Y][i] < 0:
                result[Y][i] = 0
    return result


def NGLostManN_2(NYrs, NGAppManN, NGAppNRate, LossFactAdj, NGPctSoilIncRate):
    result = np.tile(NGAppManN * NGAppNRate * ( 1 - NGPctSoilIncRate ) ,NYrs) * np.ndarray.flatten(LossFactAdj)
    result = np.minimum(result, np.tile( NGAppManN, NYrs))
    result = np.maximum(result, 0)
    return np.reshape(result,(NYrs,12))


def LossFactAdj(NYrs, Precipitation, DaysMonth):
    result = np.zeros((NYrs, 12))
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = (Precipitation[Y][i] / DaysMonth[Y][i]) / 0.3301
    return result


def LossFactAdj_2(NYrs, Precipitation, DaysMonth):
    result = Precipitation / DaysMonth / 0.3301
    return result
