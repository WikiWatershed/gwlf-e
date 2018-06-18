import hashlib

from numpy import ndarray

def memoize_with_args(f):
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

def memoize(f):
    class memodict(dict):
        def __init__(self, f):
            self.f = f
            self.result = None
            self.__name__ = f.__name__

        def __call__(self, *args):
            if self.result is None:
                ret = self.result = self.f(*args)
                return ret
            return self.result

    return memodict(f)