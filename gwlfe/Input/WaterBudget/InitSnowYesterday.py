from gwlfe.Memoization import memoize

try:
    from .InitSnowYesterday_inner_compiled import InitSnowYesterday_inner
except ImportError:
    print("Unable to import compiled InitSnowYesterday_inner, using slower version")
    from gwlfe.Input.WaterBudget.InitSnowYesterday_inner import InitSnowYesterday_inner


@memoize
def InitSnowYesterday(NYrs, DaysMonth, InitSnow_0, Temp, Prec):
    return InitSnowYesterday_inner(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
