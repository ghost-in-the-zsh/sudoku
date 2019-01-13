#!/usr/bin/env python3

'''
'''

import time

from functools import wraps

from sudoku.utils import clear_screen



def _show_board(*args):
    board = args[0]
    clear_screen()
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
