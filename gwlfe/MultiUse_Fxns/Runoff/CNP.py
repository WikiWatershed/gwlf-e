from numpy import zeros

from gwlfe.Input.LandUse.NLU import NLU
from gwlfe.Memoization import memoize


@memoize
def CNP(NRur, NUrb, CNP_0):
    nlu = NLU(NRur, NUrb)
    result = zeros((3, nlu))
    for l in range(NRur, nlu):
        result[0][l] = CNP_0[1][l] / (2.334 - 0.01334 * CNP_0[1][1])
        result[1][l] = CNP_0[1][l]
        result[2][l] = CNP_0[1][l] / (0.4036 + 0.0059 * CNP_0[1][l])
    return result


@memoize
def CNP_f(NRur, NUrb, CNP_0):
    nlu = NLU(NRur, NUrb)
    result = zeros((3, nlu))
    result[0] = CNP_0[1] / (2.334 - 0.01334 * CNP_0[1][1])
    result[1] = CNP_0[1]
    result[2] = CNP_0[1] / (0.4036 + 0.0059 * CNP_0[1])
    return result
