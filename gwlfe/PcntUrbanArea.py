import numpy as np
from Timer import time_function
from AreaTotal import AreaTotal
from UrbAreaTotal import UrbAreaTotal
from Memoization import memoize
from AreaTotal import AreaTotal_2
from UrbAreaTotal import UrbAreaTotal_2


# @memoize
def PcntUrbanArea(NRur, NUrb, Area):
    result = 0
    areatotal = AreaTotal(NRur, NUrb, Area)
    urbareatotal = UrbAreaTotal(NRur, NUrb, Area)
    if areatotal == 0:
        result = 0
    else:
        result += urbareatotal / areatotal
    return result


def PcntUrbanArea_2(NRur, NUrb, Area):
    result = 0
    areatotal = AreaTotal_2(Area)
    urbareatotal = UrbAreaTotal_2(NRur, NUrb, Area)
    if areatotal != 0:
        result += urbareatotal / areatotal
    return result
