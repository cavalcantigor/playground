"""
    Implementation based on: https://dbader.org/blog/python-memoization

    Basic memoization algorithm:
        1. Set up a cache data structure for function results
        2. Every time the function is called, do one of the following:
            - return cached result, if any; or
            - call function to compute missing result and then update the cache
                before returning result to the caller
"""
import functools
import timeit


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func


@memoize
def memoized_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


@functools.lru_cache(maxsize=128)
def lru_cache_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return lru_cache_fibonacci(n - 1) + lru_cache_fibonacci(n - 2)


if __name__ == '__main__':
    print(str(timeit.timeit('fibonacci(35)', globals=globals(), number=1)))             # 3.375589
    print(str(timeit.timeit('fibonacci(35)', globals=globals(), number=1)))             # 3.529400
    print(str(timeit.timeit('memoized_fibonacci(35)', globals=globals(), number=1)))    # 3.88e-05
    print(str(timeit.timeit('memoized_fibonacci(35)', globals=globals(), number=1)))    # 9.12e-07
    print(str(timeit.timeit('lru_cache_fibonacci(35)', globals=globals(), number=1)))   # 2.74e-06
    print(str(timeit.timeit('lru_cache_fibonacci(35)', globals=globals(), number=1)))   # 7.19e-07
