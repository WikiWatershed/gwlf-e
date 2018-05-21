from Memoization import memoize
from Timer import time_function
from time import sleep

@time_function
def test_function():
    return memoizied_function()

@memoize
def memoizied_function():
    sleep(0.3)
    return 2+2

if __name__ == "__main__":
    print(test_function())