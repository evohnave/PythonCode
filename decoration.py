# Nice decorator for timing functions

from functools import wraps
from time import time

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print(f'func:%r args:%r, kwargs:%r took: %2.4f sec' % \
          (f.__name__, args, kw, te-ts))
        return result
    return wrap

