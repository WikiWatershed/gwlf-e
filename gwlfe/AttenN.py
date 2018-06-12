# from Timer import time_function
from FlowDays import FlowDays
from Memoization import memoize


@memoize
def AttenN(AttenFlowDist, AttenFlowVel, AttenLossRateN):
    return FlowDays(AttenFlowDist, AttenFlowVel) * AttenLossRateN

# def AttenN_2():
#     pass
