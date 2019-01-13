#!/usr/bin/env python3

'''
'''

import os, time

from functools import wraps


_clear = 'clear' if os.name is not 'nt' else 'cls'


def _show_board(*args):
    board = args[0]
    os.system(_clear)
    print(str(board))


def visualizer(func, delay_secs):
    @wraps(func)
    def visualizer_wrapper(*args, **kwargs):
        _show_board(*args)
        time.sleep(delay_secs)
        value = func(*args, **kwargs)
        _show_board(*args)
        return value
    return visualizer_wrapper


def benchmark(func):
    @wraps(func)
    def benchmark_wrapper(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        delta = time.perf_counter() - start
        print(f'Finished {func.__name__!r} in {delta:.4f} secs')
        return value
    return benchmark_wrapper
