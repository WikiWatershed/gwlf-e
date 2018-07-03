# from Timer import time_function
from gwlfe.Memoization import memoize


@memoize
def SedDelivRatio(SedDelivRatio_0):
    if SedDelivRatio_0 == 0:
        result = 0.0001
    else:
        result = SedDelivRatio_0
    return result

# def SedDelivRatio_f():
#     pass
