import hashlib

from numpy import ndarray


def memoize_with_args(f):
    """This memoization function checks to ensure that the called arguments are equal before returning memoized result.
    This is patched in for testing to ensure that there is less chance of unitentional coupling, but it comes at the
    expense of some performance"""

    class memodict():
        def __init__(self, f):
            self.f = f
            self.result = {}
            self.__name__ = f.__name__

        def __call__(self, *args):
            args_string = f.__name__
            for arg in args:
                if (isinstance(arg, ndarray)):
                    args_string += hashlib.sha1(arg).hexdigest() + ","
                else:
                    args_string += hashlib.sha1(str(arg)).hexdigest() + ","
            try:
                return self.result[args_string]
            except KeyError:
                self.result[args_string] = self.f(*args)
                return self.result[args_string]

    return memodict(f)


# def memoize(f): #use this function to disable memoization
#     return f

memoized_return_values = {}


def resetMemoization():
    global memoized_return_values
    memoized_return_values = {}


def memoize(f):
    """This memoization function does not check what arguments the function is called with. This requires that the model
    be reitinitalized between each run, but saves a significant amount of time on a single run"""

    class memodict(dict):
        def __init__(self, f):
            self.f = f
            self.__name__ = f.__name__

        def __call__(self, *args):
            global memoized_return_values
            try:
                return memoized_return_values[self.__name__]
            except KeyError:
                ret = memoized_return_values[self.__name__] = self.f(*args)
                return ret

    return memodict(f)
