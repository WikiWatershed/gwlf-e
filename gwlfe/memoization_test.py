from Timer import time_function
from time import sleep
from Memoization import *
from HashableArray import HashableArray

@memoize
def test(a,b,c,d,e,f,g,h,i,j):
    sleep(0.03)
    return 3

@time_function
def test_test():
    temp = HashableArray(range(0, 1000))
    for i in range(0, 100):
        test(temp, temp, temp, temp, temp, temp, temp, temp, temp, temp)

if __name__ == "__main__":
    test_test()