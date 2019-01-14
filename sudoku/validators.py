#!/usr/bin/env python3

'''Validators module to work with argparse options.'''

import argparse as ap


def real_positive_number(s: str) -> float:
    '''Validates that the input is a positive real number.'''
    msg = 'value must be a positive real number'
    try:
        n = float(s)
        if n <= 0:
            raise ap.ArgumentTypeError(msg)
        return n
    except ValueError:
        raise ap.ArgumentTypeError(msg)
