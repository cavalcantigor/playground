### Memoization

Memoization (not memorization) is a technique for improving
algorithms performance. Once a solution for a 
deterministic problem is found, then is cached. Cache
is used to speed up future calls to the function that
calculates the problem result. Example: fibonacci.

Python implementation with `lru_cache` and `decorators`
can be found [here](memo-python.py).

[Here](https://stackoverflow.com/questions/6184869/what-is-the-difference-between-memoization-and-dynamic-programming)
you can see that *Dynamic Programming* and *Memoization*
are ***NOT*** the same thing.