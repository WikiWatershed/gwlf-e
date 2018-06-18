import hashlib

from numpy import ndarray


# without
# 300 loops of 'test_test', average time per loop: 0.321625, best: 0.303278, worst: 0.426772
# 300 loops of 'test_test', average time per loop: 0.006865, best: 0.001217, worst: 0.016353
# def memoize_with_args(f):
#     return f

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


# 300 loops of 'test_test', average time per loop: 0.000156, best: 0.000117, worst: 0.000521
# def memoize(f):
#     class memodict():
#         def __init__(self, f):
#             self.f = f
#             self.result = None
#         def __call__(self,*args):
#             # if self.result is None:
#             #     ret = self.result = self.f(*args)
#             #     return ret
#             return self.f(*args)
#     return memodict(f)


def memodict(f):
    class memodict(dict):
        def __missing__(self, *args):
            ret = self['result'] = f(*args)
            return ret

        def __getitem__(self, *args):
            return dict.__getitem__(self, 'result')

    return memodict().__getitem__


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