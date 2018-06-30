from gwlfe.Memoization import memoize


@memoize
def FlowDays(AttenFlowDist, AttenFlowVel):
    if AttenFlowDist > 0 and AttenFlowVel > 0:
        return AttenFlowDist / (AttenFlowVel * 24)
    else:
        return 0

# def FlowDays_f():
#     pass
