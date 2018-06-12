# from Timer import time_function
from numpy import sum
from CNI import CNI
from CNP import CNP
from Memoization import memoize
from NLU import NLU
from UrbAreaTotal import UrbAreaTotal


# @time_function
@memoize
def AvCNUrb(NRur, NUrb, CNI_0, CNP_0, Imper, Area):
    result = 0
    nlu = NLU(NRur, NUrb)
    cni = CNI(NRur, NUrb, CNI_0)
    cnp = CNP(NRur, NUrb, CNP_0)
    urbareatotal = UrbAreaTotal(NRur, NUrb, Area)
    for l in range(NRur, nlu):
        # Calculate average area-weighted CN for urban areas
        if urbareatotal > 0:
            result += ((Imper[l] * cni[1][l] + (1 - Imper[l]) * cnp[1][l]) * Area[l] / urbareatotal)
    return result

# Tried, slower than original.
# @time_function
def AvCNUrb_2(NRur, NUrb, CNI_0, CNP_0, Imper, Area):
    cni = CNI(NRur, NUrb, CNI_0)
    cnp = CNP(NRur, NUrb, CNP_0)
    urbareatotal = UrbAreaTotal(NRur, NUrb, Area)
    temp = ((Imper* cni[1] + (1 - Imper) * cnp[1]) * Area / urbareatotal)[NRur:]
    return sum(temp)

