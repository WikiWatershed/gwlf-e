import numpy as np
# from Timer import time_function
from Memoization import memoize

@memoize
def RetentFactorN(ShedAreaDrainLake, RetentNLake):
    return (1 - (ShedAreaDrainLake * RetentNLake))

# def RetentFactorN_2():
#     pass
