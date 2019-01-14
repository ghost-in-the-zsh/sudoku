#!/usr/bin/env python3

'''Utilities module for stand-alone functions.'''

import os


_clear_command = 'cls' if os.name is 'nt' else 'clear'


def clear_screen():
    os.system(_clear_command)
