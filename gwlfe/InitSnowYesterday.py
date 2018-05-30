try:
    from InitSnowYesterday_inner_compiled import InitSnowYesterday_inner
except ImportError:
    print("Unable to import compiled InitSnowYesterday_inner, using slower version")
    from InitSnowYesterday_inner import InitSnowYesterday_inner


def InitSnowYesterday(NYrs, DaysMonth, InitSnow_0, Temp, Prec):
    return InitSnowYesterday_inner(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
