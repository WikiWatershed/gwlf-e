from gwlfe.Input.LandUse.AreaTotal import AreaTotal
from gwlfe.Input.LandUse.RurAreaTotal import RurAreaTotal
from gwlfe.Input.LandUse.Urb.UrbAreaTotal import UrbAreaTotal
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Runoff.AvCNRur import AvCNRur
from gwlfe.MultiUse_Fxns.Runoff.AvCNUrb import AvCNUrb


@memoize
def AvCN(NRur, NUrb, CNI_0, CNP_0, CN, Imper, Area):
    result = 0
    urbareatotal = UrbAreaTotal(NRur, NUrb, Area)
    rurareatotal = RurAreaTotal(NRur, Area)
    areatotal = AreaTotal(NRur, NUrb, Area)
    avcnurb = AvCNUrb(NRur, NUrb, CNI_0, CNP_0, Imper, Area)
    avcnrur = AvCNRur(NRur, Area, CN)
    # Calculate the average CN
    if areatotal == 0:
        result += 0
    else:
        result += ((avcnrur * rurareatotal / areatotal) + (avcnurb * urbareatotal / areatotal))
    return result


def AvCN_f(NRur, NUrb, CNI_0, CNP_0, CN, Imper, Area):
    areatotal = AreaTotal(NRur, NUrb, Area)
    # Calculate the average CN
    if areatotal == 0:
        return 0
    else:
        urbareatotal = UrbAreaTotal(NRur, NUrb, Area)
        rurareatotal = RurAreaTotal(NRur, Area)
        avcnurb = AvCNUrb(NRur, NUrb, CNI_0, CNP_0, Imper, Area)
        avcnrur = AvCNRur(NRur, Area, CN)
        return ((avcnrur * rurareatotal / areatotal) + (avcnurb * urbareatotal / areatotal))
