from gwlfe.Memoization import memoize


@memoize
def AGSTRM(AgLength, StreamLength):
    # OBTAIN THE LENGTH OF STREAMS IN AGRICULTURAL AREAS
    result = 0.0
    result = AgLength / StreamLength if StreamLength > 0 else 0
    return result


@memoize
def AGSTRM_f(AgLength, StreamLength):
    # OBTAIN THE LENGTH OF STREAMS IN AGRICULTURAL AREAS
    if (StreamLength > 0):
        return AgLength / StreamLength
    else:
        return 0
