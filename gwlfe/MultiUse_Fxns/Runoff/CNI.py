from numpy import zeros

from gwlfe.Input.LandUse.NLU import NLU
from gwlfe.Memoization import memoize


@memoize
def CNI(NRur, NUrb, CNI_0):
    nlu = NLU(NRur, NUrb)
    result = zeros((3, nlu))
    for l in range(NRur, nlu):
        result[0][l] = CNI_0[1][l] / (2.334 - 0.01334 * CNI_0[1][1])
        result[1][l] = CNI_0[1][l]
        result[2][l] = CNI_0[1][l] / (0.4036 + 0.0059 * CNI_0[1][l])
    return result


@memoize
def CNI_f(NRur, NUrb, CNI_0):
    nlu = NLU(NRur, NUrb)
    result = zeros((3, nlu))
    result[0] = CNI_0[1] / (2.334 - 0.01334 * CNI_0[1][1])
    result[1] = CNI_0[1]
    result[2] = CNI_0[1] / (0.4036 + 0.0059 * CNI_0[1])
    return result
