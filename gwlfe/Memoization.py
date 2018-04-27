# without
# 300 loops of 'test_test', average time per loop: 0.321625, best: 0.303278, worst: 0.426772
# 300 loops of 'test_test', average time per loop: 0.006865, best: 0.001217, worst: 0.016353
def memoize_with_args(f):
    memo = {}

    def helper(*args):
        if str(args) not in memo:
            memo[str(args)] = f(*args)
        return memo[str(args)]

    return helper


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

def memoize(f):
    class memodict():
        def __init__(self, f):
            self.f = f
            self.result = None

        def __call__(self, *args):
            if self.result is None:
                ret = self.result = self.f(*args)
                return ret
            return self.result

    return memodict(f)

# def memoize_list(f):
#     """ Memoization decorator for functions taking one or more arguments. """
#     class memodict(dict):
#         def __init__(self, f):
#             self.f = f
#         def __call__(self):
#             return self[args]
#         def __missing__(self, key):
#             ret = self[key] = self.f(*key)
#             return ret
#     return memodict(f)
