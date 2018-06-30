from gwlfe.Input.WaterBudget.FlowDays import FlowDays
from gwlfe.Memoization import memoize


@memoize
def AttenN(AttenFlowDist, AttenFlowVel, AttenLossRateN):
    return FlowDays(AttenFlowDist, AttenFlowVel) * AttenLossRateN

# def AttenN_f():
#     pass
