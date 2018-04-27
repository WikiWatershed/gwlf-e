import numpy as np
from Timer import time_function
from NLU import NLU
from CNI import CNI
from CNP import CNP
from UrbAreaTotal import UrbAreaTotal

from Memoization import memoize


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


def AvCNUrb_2():
    pass
