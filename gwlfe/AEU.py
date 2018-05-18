import numpy as np
from Timer import time_function
from AreaTotal import AreaTotal
from TotLAEU import TotLAEU
from Memoization import memoize
from AreaTotal import AreaTotal_2


def AEU(NumAnimals, AvgAnimalWt, NRur, NUrb, Area):
    result = 0
    areatotal = AreaTotal(NRur, NUrb, Area)
    totLAEU = TotLAEU(NumAnimals, AvgAnimalWt)
    if totLAEU > 0 and areatotal > 0:
        result += totLAEU / (areatotal * 2.471)
    else:
        result = 0
    return result


def AEU_2(NumAnimals, AvgAnimalWt, NRur, NUrb, Area):
    result = 0
    areatotal = AreaTotal_2(Area)
    totLAEU = TotLAEU(NumAnimals, AvgAnimalWt)
    if totLAEU > 0 and areatotal > 0:
        result += totLAEU / (areatotal * 2.471)
    else:
        result = 0
    return result
