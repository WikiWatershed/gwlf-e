from numpy import where
from numpy import zeros

from gwlfe.Input.LandUse.NLU import NLU
from gwlfe.Memoization import memoize


@memoize
def NewCN(NRur, NUrb, CN):
    nlu = NLU(NRur, NUrb)
    result = zeros((3, nlu))
    for l in range(NRur):
        result[0][l] = CN[l] / (2.334 - 0.01334 * CN[l])
        result[2][l] = CN[l] / (0.4036 + 0.0059 * CN[l])
        if result[2][l] > 100:
            result[2][l] = 100
    return result


@memoize
def NewCN_f(NRur, NUrb, CN):
    nlu = NLU(NRur, NUrb)
    result = zeros((3, nlu))
    result[0, :] = CN / (2.334 - 0.01334 * CN)
    result[2, :] = CN / (0.4036 + 0.0059 * CN)
    result[2, :][where(result[2, :] > 100)] = 100
    return result
