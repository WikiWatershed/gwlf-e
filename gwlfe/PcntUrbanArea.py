# from Timer import time_function
from AreaTotal import AreaTotal
from AreaTotal import AreaTotal_f
from UrbAreaTotal import UrbAreaTotal
from UrbAreaTotal import UrbAreaTotal_f


def PcntUrbanArea(NRur, NUrb, Area):
    result = 0
    areatotal = AreaTotal(NRur, NUrb, Area)
    urbareatotal = UrbAreaTotal(NRur, NUrb, Area)
    if areatotal == 0:
        result = 0
    else:
        result += urbareatotal / areatotal
    return result


def PcntUrbanArea_f(NRur, NUrb, Area):
    areatotal = AreaTotal_f(Area)
    if areatotal != 0:
        return UrbAreaTotal_f(NRur, NUrb, Area) / areatotal
    else:
        return 0
