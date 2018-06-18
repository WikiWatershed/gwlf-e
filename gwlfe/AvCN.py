# from Timer import time_function
from AreaTotal import AreaTotal
from AvCNRur import AvCNRur
from AvCNUrb import AvCNUrb
from Memoization import memoize
from RurAreaTotal import RurAreaTotal
from UrbAreaTotal import UrbAreaTotal


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

# @time_function #vecotrized version was slower
# def AvCN_f(NRur, NUrb, CNI_0, CNP_0, CN, Imper, Area):
#     # Calculate the average CN
#     areatotal = AreaTotal_f(Area)
#     if (areatotal > 0):
#         urbareatotal = UrbAreaTotal_f(NRur, NUrb, Area)
#         rurareatotal = RurAreaTotal_f(NRur, Area)
#
#         avcnurb = AvCNUrb_f(NRur, NUrb, CNI_0, CNP_0, Imper, Area)
#         avcnrur = AvCNRur_f(NRur, Area, CN)
#         return ((avcnrur * rurareatotal / areatotal) + (avcnurb * urbareatotal / areatotal))
#
#     else:
#         return 0
