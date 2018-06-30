from numpy import zeros

from gwlfe.Input.WaterBudget.Grow import Grow_f
from gwlfe.Memoization import memoize
from gwlfe.enums import GROWING_SEASON


@memoize
def GrowFactor(Grow_0):
    result = zeros((12,))
    for i in range(12):
        result[i] = Grow_0[i] == GROWING_SEASON  # TODO: seems like there is some inefficency left in Grow_0
    return result


@memoize
def GrowFactor_f(Grow_0):
    return Grow_f(Grow_0)
