from numpy import sum

from gwlfe.Input.LandUse.NLU import NLU
from gwlfe.Input.LandUse.Urb.UrbAreaTotal import UrbAreaTotal
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Runoff.CNI import CNI
from gwlfe.MultiUse_Fxns.Runoff.CNP import CNP


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


def AvCNUrb_f(NRur, NUrb, CNI_0, CNP_0, Imper, Area):
    cni = CNI(NRur, NUrb, CNI_0)
    cnp = CNP(NRur, NUrb, CNP_0)
    urbareatotal = UrbAreaTotal(NRur, NUrb, Area)
    temp = ((Imper * cni[1] + (1 - Imper) * cnp[1]) * Area / urbareatotal)[NRur:]
    return sum(temp)
