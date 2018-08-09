from gwlfe.Memoization import memoize


@memoize
def FilterEff(FilterWidth):
    if FilterWidth <= 30:
        result = FilterWidth / 30
    else:
        result = 1
    return result


# Both have same running time
@memoize
def FilterEff_f(FilterWidth):
    result = 1
    if FilterWidth <= 30:
        result = FilterWidth / 30
    return result
