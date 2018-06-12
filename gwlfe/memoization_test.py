from Memoization import memoize
from Memoization import memoize_with_args
from Memoization import memoize2
# from Timer import time_function
from time import sleep
import numpy as np


@time_function
def test_function1():
    test = np.ones((1000, 1000))
    return memoizied_function(test, test, test, test, test, test, test, test, test, test, test, test, test, test, test,
                              test, test, test, test, test, )


@memoize_with_args
def memoizied_function(*arg):
    sleep(0.3)
    return np.random.random((1000, 1000))

@time_function
def test_function2():
    test = np.ones((1000, 1000))
    return memoizied_function2(test, test, test, test, test, test, test, test, test, test, test, test, test, test, test,
                              test, test, test, test, test, )


@memoize
def memoizied_function2(*arg):
    sleep(0.3)
    return np.random.random((1000, 1000))

@time_function
def test_function3():
    test = np.ones((1000, 1000))
    return memoizied_function3(test, test, test, test, test, test, test, test, test, test, test, test, test, test, test,
                              test, test, test, test, test, )


@memoize
def memoizied_function3(*arg):
    sleep(0.3)
    return np.random.random((1000, 1000))


if __name__ == "__main__":
    test_function1()
    test_function2()
    test_function3()
