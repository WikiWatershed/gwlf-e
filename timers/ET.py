import timeit
import os
from gwlfe import Parser
from gwlfe import ET

basepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
setup = """
from __main__ import ET
from __main__ import parser
fp = open('"""+basepath+'/test/input_4.gms'+"""', 'r')
z = parser.GmsReader(fp).read()
"""

if __name__ == "__main__":
    old_fun = timeit.Timer('ET.DailyET(z.NYrs,z.DaysMonth,z.Temp,z.DayHrs,z.KV,z.PcntET,z.ETFlag)', setup=setup)
    new_fun = timeit.Timer('ET.DailyET_2(z.Temp,z.KV,z.PcntET,z.DayHrs)', setup=setup)
    try:
        print("10000 loops, time per loop: "+str(old_fun.timeit(number=100)/100)) # or t.repeat(...)
        print("10000 loops, time per loop: "+str(new_fun.timeit(number=100)/100)) # or t.repeat(...)
    except:
        old_fun.print_exc()
        new_fun.print_exc()