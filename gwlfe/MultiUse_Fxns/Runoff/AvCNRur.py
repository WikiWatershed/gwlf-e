from numpy import sum

from gwlfe.Input.LandUse.RurAreaTotal import RurAreaTotal
from gwlfe.Input.LandUse.RurAreaTotal import RurAreaTotal_f
from gwlfe.Memoization import memoize


@memoize
def AvCNRur(NRur, Area, CN):
    result = 0
    rurareatotal = RurAreaTotal(NRur, Area)
    # Get the area weighted average CN for rural areas
    for l in range(NRur):
        # Calculate average area weighted CN and KF
        result += (CN[l] * Area[l] / rurareatotal) if rurareatotal > 0 else 0
    return result


def AvCNRur_f(NRur, Area, CN):
    rurareatotal = RurAreaTotal_f(NRur, Area)
    if (rurareatotal > 0):
        return sum(CN * Area / rurareatotal)
    else:
        return 0
