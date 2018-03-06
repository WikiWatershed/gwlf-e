import numpy as np
from Timer import time_function


def GRAppManN(GRPctManApp, InitGrN):
    result = np.zeros((12,))
    for i in range(12):
        result[i] = GRPctManApp[i] * InitGrN
    return result


def GrAppManN_2():
    pass


def GrazingN(PctGrazing, InitGrN):
    result = np.zeros((12,))
    for i in range(12):
        result[i] = PctGrazing[i] * (InitGrN / 12)
    return result


def GrazingN_2():
    pass


def GRAccManAppN(InitGrN, GRPctManApp, GrazingN):
    result = np.zeros((12,))
    for i in range(12):
        result[i] = (result[i] + (InitGrN / 12)
                     - (GRPctManApp[i] * InitGrN) - GrazingN[i])
        if result[i] < 0:
            result[i] = 0
    return result


def GRAccManAppN_2():
    pass


def GRInitBarnN(GRAppManN, InitGrN, GRPctManApp, GrazingN):
    result = np.zeros((12,))
    grAccManAppN = GRAccManAppN(InitGrN, GRPctManApp, GrazingN)
    for i in range(12):
        result[i] = grAccManAppN[i] - GRAppManN[i]
    return result


def GRInitBarnN_2():
    pass


def LossFactAdj(NYrs, Precipitation, DaysMonth):
    result = np.zeros((NYrs, 12))
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = (Precipitation[Y][i] / DaysMonth[Y][i]) / 0.3301
    return result


def LossFactAdj_2():
    pass


def NGLostBarnN(NYrs, NGInitBarnN, NGBarnNRate, LossFactAdj, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN):
    result = np.zeros((NYrs, 12))
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = (NGInitBarnN[i] * NGBarnNRate[i] * LossFactAdj[Y][i]
                            - NGInitBarnN[i] * NGBarnNRate[i] * LossFactAdj[Y][i] * AWMSNgPct * NgAWMSCoeffN
                            + NGInitBarnN[i] * NGBarnNRate[i] * LossFactAdj[Y][i] * RunContPct * RunConCoeffN)
    return result


def NGLostBarnN_2():
    pass


def NGLostManN(NYrs, NGAppManN, NGAppNRate, LossFactAdj, NGPctSoilIncRate):
    # Non-grazing animal losses
    result = np.zeros((NYrs, 12))
    for Y in range(NYrs):
        for i in range(12):
            # I think all these conditions are unnecessary
            if result[Y][i] > NGAppManN[i]:
                result[Y][i] = NGAppManN[i]
            if result[Y][i] < 0:
                result[Y][i] = 0
            result[Y][i] = (NGAppManN[i] * NGAppNRate[i] * LossFactAdj[Y][i]
                            * (1 - NGPctSoilIncRate[i]))
    return result


def NGLostManN_2():
    pass


def GRLostManN(NYrs, GRAppManN, GRAppNRate, LossFactAdj, GRPctSoilIncRate):
    result = np.zeros((NYrs, 12))
    for Y in range(NYrs):
        for i in range(12):
            if result[Y][i] > GRAppManN[i]:
                result[Y][i] = GRAppManN[i]
            if result[Y][i] < 0:
                result[Y][i] = 0
            result[Y][i] = (GRAppManN[i] * GRAppNRate[i] * LossFactAdj[Y][i] * (1 - GRPctSoilIncRate[i]))
    return result


def GRLostManN_2():
    pass
