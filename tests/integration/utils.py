"""Utilities for integration tests."""
import time


def call_function(func, num_times: int, rate: int, *args):  # noqa: ANN002
    """Call 'func' 'num_times' times at 'rate' times per second."""
    results = []

    for _ in range(num_times):
        start_time = time.time()
        results.append(func(*args))
        time.sleep(max(1 / rate - (time.time() - start_time), 0))

    return results
