import numpy as np
from Timer import time_function
from AreaTotal import AreaTotal
from UrbAreaTotal import UrbAreaTotal
from UrbAreaTotal import UrbAreaTotal_2
from RurAreaTotal import RurAreaTotal
from RurAreaTotal import RurAreaTotal_2
from AvCNUrb import AvCNUrb
from AvCNUrb import AvCNUrb_2
from AvCNRur import AvCNRur
from AvCNRur import AvCNRur_2
from Memoization import memoize
from AreaTotal import AreaTotal_2


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
# def AvCN_2(NRur, NUrb, CNI_0, CNP_0, CN, Imper, Area):
#     # Calculate the average CN
#     areatotal = AreaTotal_2(Area)
#     if (areatotal > 0):
#         urbareatotal = UrbAreaTotal_2(NRur, NUrb, Area)
#         rurareatotal = RurAreaTotal_2(NRur, Area)
#
#         avcnurb = AvCNUrb_2(NRur, NUrb, CNI_0, CNP_0, Imper, Area)
#         avcnrur = AvCNRur_2(NRur, Area, CN)
#         return ((avcnrur * rurareatotal / areatotal) + (avcnurb * urbareatotal / areatotal))
#
#     else:
#         return 0
