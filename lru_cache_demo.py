from functools import lru_cache

@lru_cache()
def fib(N):
    if N != abs(int(N)):
        raise ValueError("N must be a positive integer!")
    elif N in [0, 1]:
        return N
    else:
        return fib(N - 2) + fib(N - 1)


