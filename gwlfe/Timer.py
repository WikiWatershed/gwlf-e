import timeit
import numpy as np
from copy import deepcopy


def time_function(method):
    def timed(*args, **kw):
        """return the result of the function as well as timing results for it"""

        def reset_scope():
            method.result = None  # for memoized functions

        function_to_time = timeit.Timer(lambda: method(*args), setup=reset_scope)
        runs = function_to_time.repeat(number=1, repeat=300)
        print("300 loops of %r, average time per loop: %f, best: %f, worst: %f" % (
            method.__name__, np.average(runs), np.min(runs), np.max(runs)))

        result = method(*args, **kw)
        return result

    return timed
