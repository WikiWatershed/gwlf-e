import timeit
from gwlfe import parser
from gwlfe import Precipitation


setup = """
from __main__ import Precipitation
from __main__ import parser
fp = open('C:/Users/Austin/Documents/GitHub/gwlf-e/test/input_4.gms', 'r')
z = parser.GmsReader(fp).read()

"""

if __name__ == "__main__":
    old_fun = timeit.Timer('Precipitation.Precipitation(z.NYrs, z.DaysMonth, z.Prec)', setup=setup)
    new_fun = timeit.Timer('Precipitation.Precipitation_2(Precipitation.Prec_to_numpy(z.Prec))', setup=setup)
    try:
        print("10000 loops, time per loop: "+str(old_fun.timeit(number=10000)/10000)) # or t.repeat(...)
        print("10000 loops, time per loop: "+str(new_fun.timeit(number=10000)/10000)) # or t.repeat(...)
    except:
        old_fun.print_exc()
        new_fun.print_exc()