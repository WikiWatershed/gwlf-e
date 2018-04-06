import numpy as np
from Timer import time_function
from NLU import NLU

def UrbAreaTotal(NRur,NUrb,Area):
    result = 0
    nlu = NLU(NRur,NUrb)
    for l in range(NRur, nlu):
        result += Area[l]
    return result


def UrbAreaTotal_2():
    pass
