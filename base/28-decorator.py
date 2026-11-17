from datetime import datetime
from functools import wraps
from time import perf_counter


def seconds_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).total_seconds())


def calculate_run_time(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        before_time = perf_counter()
        try:
            return f(*args, **kwargs)
        finally:
            elapsed = perf_counter() - before_time
            print(f"{f.__name__} took {elapsed:.6f} seconds")

    return wrapper


@calculate_run_time
def create_number_list(n):
    return list(range(n))


if __name__ == "__main__":
    print(create_number_list(5))
