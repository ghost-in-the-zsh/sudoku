#!/usr/bin/env python3

'''Function decorators module.

Decorators in this module allow dynamically adding responsibilities
to existing functionality while keeping original functionality intact
and decoupled. This includes benchmarking and visualization features.
'''

import time

from typing import Callable
from functools import wraps

from sudoku.utils import clear_screen


def _show_board(*args, depth, calls):
    board = args[0]
    clear_screen()
    print(str(board))
    print(f'depth={depth}, calls={calls:,}')


def visualizer(func: Callable, delay_secs: int) -> Callable:
    recursion_depth = 0
    recursion_calls = 0
    @wraps(func)
    def visualizer_wrapper(*args, **kwargs):
        nonlocal recursion_depth
        nonlocal recursion_calls
        _show_board(*args, depth=recursion_depth, calls=recursion_calls)
        time.sleep(delay_secs)
        recursion_depth += 1
        recursion_calls += 1
        func(*args, **kwargs)
        recursion_depth -= 1
        _show_board(*args, depth=recursion_depth, calls=recursion_calls)
    return visualizer_wrapper


def benchmark(func: Callable) -> Callable:
    @wraps(func)
    def benchmark_wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        delta = time.perf_counter() - start
        return delta
    return benchmark_wrapper
