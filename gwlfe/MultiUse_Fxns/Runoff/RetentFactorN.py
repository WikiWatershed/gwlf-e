from gwlfe.Memoization import memoize


@memoize
def RetentFactorN(ShedAreaDrainLake, RetentNLake):
    return (1 - (ShedAreaDrainLake * RetentNLake))

# def RetentFactorN_f():
#     pass
