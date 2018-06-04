import numpy as np
from gwlfe.Timer import time_function


# def AvPrecipitation(NYrs, Precipitation):
#     result = np.zeros((12,))
#     for Y in range(NYrs):
#         for i in range(12):
#             result[i] += Precipitation[Y][i] / NYrs
#     return result
#
#
# def AvPrecipitation_2(Precipitation):
#     return np.average(Precipitation, axis=0)
