from collections import defaultdict
import functools
import time


def debugging(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        _fname = f"[{f.__name__}]"

        print(f"Calling > {_fname}")
        print(f" . type  : {type(f)}")
        print(f" . args  : {args}")
        print(f" . kwargs: {kwargs}")

        result = f(*args, **kwargs)

        print()
        print(f"Executed > {_fname}")
        print(f" . Returned: {result}")
        return result

    return wrapper


# Timing Purposes in Python
def timeit(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        # In Python, you can use the time module to measure elapsed time.
        # You can use the time() function to get the current time in seconds since the epoch (January 1, 1970, at 00:00:00 UTC).
        # Then, you can subtract the start time from the end time to get the elapsed time.

        # Alternatively, you can use the perf_counter() or monotonic() function to measure the time, that depends on the specific use case:

        start_time = time.perf_counter()
        result = f(*args, **kwargs)
        end_time = time.perf_counter()

        elapsed_time = round(end_time - start_time, ndigits=3)
        print(f"Time executed {f.__name__!r} is {elapsed_time!r}")
        print(f" . Start time: {start_time}")
        print(f" . End   time: {end_time}")
        return result

    return wrapper


def check_type(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        # iterate over the function arguments and their types
        for _arg, _argtype in zip(args, f.__annotations__.values()):
            if not isinstance(_arg, _argtype):
                raise TypeError(f"Argument {_arg} has incorrect type {type(_arg)}")

        result = f(*args, **kwargs)
        return result

    return wrapper


######################################################################
######################################################################
######################################################################

import operator as ops


@timeit
@check_type
@debugging
def add(a: int, b: int):
    return ops.add(a, b)


# print()
# print(f"Result: {add(1, 2)}")  # -> Result: 3
# print(add("1", 2))  # -> Issue


######################################################################
######################################################################
######################################################################


def make_singleton(cls):
    instances = defaultdict(dict)

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@make_singleton
class Connection:
    def __init__(self, url):
        print("Initializing connection.")
        self.url = url

    def execute(self, query):
        print(f"Executing query: {query} on {self.url}")


connect1 = Connection("https://google.com.vn").execute("GET")
connect2 = Connection("https://google.com.vn").execute("POST")
