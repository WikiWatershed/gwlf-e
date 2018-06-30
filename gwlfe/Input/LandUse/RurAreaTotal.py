from numpy import sum

from gwlfe.Memoization import memoize


# RurAreaTotal is faster
@memoize
def RurAreaTotal(NRur, Area):
    result = 0
    for l in range(NRur):
        result += Area[l]
    return result


@memoize
def RurAreaTotal_f(NRur, Area):
    return sum(Area[0:NRur])
