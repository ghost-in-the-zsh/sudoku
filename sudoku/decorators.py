#!/usr/bin/env python3

'''
'''

import time

from functools import wraps

from sudoku.utils import clear_screen


def _show_board(*args, depth):
    board = args[0]
    clear_screen()
    print(str(board))
    print('depth={}'.format(depth))


def visualizer(func, delay_secs):
    recursion_depth = 0
    @wraps(func)
    def visualizer_wrapper(*args, **kwargs):
        nonlocal recursion_depth
        _show_board(*args, depth=recursion_depth)
        time.sleep(delay_secs)
        recursion_depth += 1
        func(*args, **kwargs)
        recursion_depth -= 1
        _show_board(*args, depth=recursion_depth)
    return visualizer_wrapper


def benchmark(func):
    @wraps(func)
    def benchmark_wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        delta = time.perf_counter() - start
        return delta
    return benchmark_wrapper
