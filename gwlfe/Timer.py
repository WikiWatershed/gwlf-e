import timeit
import os

basepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
setup = """
from __main__ import parser
fp = open('""" + basepath + '/test/input_4.gms' + """', 'r')
z = parser.GmsReader(fp).read()
"""

def compare_function_calls(call_1,call_2):
    old_fun = timeit.Timer(call_1, setup=setup)
    new_fun = timeit.Timer(call_2, setup=setup)
    try:
        print("10000 loops, time per loop: " + str(old_fun.timeit(number=100) / 100))
        print("10000 loops, time per loop: " + str(new_fun.timeit(number=100) / 100))
    except:
        old_fun.print_exc()
        new_fun.print_exc()
    pass