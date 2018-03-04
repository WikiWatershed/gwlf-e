import timeit
import os
from gwlfe import Parser
from gwlfe import Precipitation

basepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
setup = """
from __main__ import Precipitation
from __main__ import parser
fp = open('"""+basepath+'/test/input_4.gms'+"""', 'r')
z = parser.GmsReader(fp).read()
"""

if __name__ == "__main__":
    old_fun = timeit.Timer('Precipitation.Precipitation(z.NYrs, z.DaysMonth, z.Prec)', setup=setup)
    new_fun = timeit.Timer('Precipitation.Precipitation_2(Precipitation.Prec_to_numpy(z.Prec))', setup=setup)
    try:
        print("10000 loops, time per loop: "+format(old_fun.timeit(number=10000)/10000, 'f'))
        print("10000 loops, time per loop: "+format(new_fun.timeit(number=10000)/10000, 'f'))
    except:
        old_fun.print_exc()
        new_fun.print_exc()