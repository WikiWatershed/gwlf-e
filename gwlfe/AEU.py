import numpy as np
from Timer import time_function
from AreaTotal import AreaTotal


def TotAEU(NumAnimals, AvgAnimalWt):
    result = 0
    aeu1 = ((NumAnimals[2] / 2) * (AvgAnimalWt[2]) / 1000) + ((NumAnimals[3] / 2) * (AvgAnimalWt[3]) / 1000)
    aeu2 = (NumAnimals[7] * AvgAnimalWt[7]) / 1000
    aeu3 = (NumAnimals[5] * AvgAnimalWt[5]) / 1000
    aeu4 = (NumAnimals[4] * AvgAnimalWt[4]) / 1000
    aeu5 = (NumAnimals[6] * AvgAnimalWt[6]) / 1000
    aeu6 = (NumAnimals[0] * AvgAnimalWt[0]) / 1000
    aeu7 = (NumAnimals[1] * AvgAnimalWt[1]) / 1000
    result += aeu1 + aeu2 + aeu3 + aeu4 + aeu5 + aeu6 + aeu7
    return result


def TotLAEU(NumAnimals, AvgAnimalWt):
    result = 0
    aeu3 = (NumAnimals[5] * AvgAnimalWt[5]) / 1000
    aeu4 = (NumAnimals[4] * AvgAnimalWt[4]) / 1000
    aeu5 = (NumAnimals[6] * AvgAnimalWt[6]) / 1000
    aeu6 = (NumAnimals[0] * AvgAnimalWt[0]) / 1000
    aeu7 = (NumAnimals[1] * AvgAnimalWt[1]) / 1000
    result += aeu3 + aeu4 + aeu5 + aeu6 + aeu7
    return result


def TotPAEU(NumAnimals, AvgAnimalWt):
    result = 0
    aeu1 = ((NumAnimals[2] / 2) * (AvgAnimalWt[2]) / 1000) + ((NumAnimals[3] / 2) * (AvgAnimalWt[3]) / 1000)
    aeu2 = (NumAnimals[7] * AvgAnimalWt[7]) / 1000
    result += aeu1 + aeu2
    return result


def AEU(NumAnimals, AvgAnimalWt, NRur, NUrb, Area):
    result = 0
    areatotal = AreaTotal(NRur, NUrb, Area)
    totLAEU = TotLAEU(NumAnimals, AvgAnimalWt)
    if totLAEU > 0 and areatotal > 0:
        result += totLAEU / (areatotal * 2.471)
    else:
        result = 0
    return result

