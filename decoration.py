# Nice decorator for timing functions

from functools import wraps
from time import time

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print(f'func: {f.__name__} args: {args}, kwargs: {kwargs} took: {ts-te:2.4f} sec')
        return result
    return wrap

