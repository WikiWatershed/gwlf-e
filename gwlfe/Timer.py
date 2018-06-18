import timeit

from numpy import array
from numpy import mean
from numpy import median


def reject_outliers(data, m=2.):
    d = abs(data - median(data))
    mdev = median(d)
    s = d / mdev if mdev else 0.
    return mean(data[s < m])


def time_function(method):
    def timed(*args, **kw):
        """return the result of the function as well as timing results for it"""

        def reset_scope():
            method.result = {}  # for memoized functions

        function_to_time = timeit.Timer(lambda: method(*args), setup=reset_scope)
        runs = function_to_time.repeat(number=1, repeat=300)
        print("300 loops of %r, average time per loop: %f, best: %f, worst: %f" % (
            method.__name__, reject_outliers(array(runs)), min(runs), max(runs)))

        result = method(*args, **kw)
        return result

    return timed
