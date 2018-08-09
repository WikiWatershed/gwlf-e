from gwlfe.Input.LandUse.AreaTotal import AreaTotal
from gwlfe.Memoization import memoize


@memoize
def TotAreaMeters(NRur, NUrb, Area):
    result = 0.0
    areatotal = AreaTotal(NRur, NUrb, Area)
    result = areatotal * 10000
    return result
