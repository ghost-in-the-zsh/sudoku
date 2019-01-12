#!/usr/bin/env python3

'''
'''

import sys
import argparse as ap

from sudoku.models import Board
from sudoku.solver import BacktrackSolver
from sudoku.validators import real_positive_number


def parse_arguments() -> ap.Namespace:
    parser = ap.ArgumentParser(description='A sudoku solver')
    parser.add_argument(
        '-f',
        '--file',
        metavar='PATH',
        type=str,
        dest='filepath',
        help='text file containing a 9x9 sudoku grid'
    )
    parser.add_argument(
        '-s',
        '--show-steps',
        dest='show_steps',
        action='store_true',
        help='shows a step-by-step run'
    )
    parser.add_argument(
        '-d',
        '--delay',
        metavar='SECS',
        type=real_positive_number,
        dest='delay_secs',
        default=0.02,
        help='delay, in seconds, when using \'--show-steps\''
    )
    return parser.parse_args()


def main():
    args   = parse_arguments()
    board  = Board(args.filepath)
    solver = BacktrackSolver()
    solver.solve(board)
    print(str(board))
    sys.exit(0)


if __name__ == '__main__':
    main()
