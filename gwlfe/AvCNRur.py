import numpy as np
from Timer import time_function
from RurAreaTotal import RurAreaTotal
from Memoization import memoize


@memoize
def AvCNRur(NRur, Area, CN):
    result = 0
    rurareatotal = RurAreaTotal(NRur, Area)
    # Get the area weighted average CN for rural areas
    for l in range(NRur):
        # Calculate average area weighted CN and KF
        result += (CN[l] * Area[l] / rurareatotal) \
            if rurareatotal > 0 else 0
    return result


def AvCNRur_2():
    pass
