import numpy as np
from Timer import time_function
from Memoization import memoize
from FlowDays import FlowDays


def AttenN(AttenFlowDist, AttenFlowVel, AttenLossRateN):
    return FlowDays(AttenFlowDist, AttenFlowVel) * AttenLossRateN

# def AttenN_2():
#     pass
