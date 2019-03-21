#!/usr/bin/env python3

'''Main sudoku solving program.'''

import sys
import argparse as ap

from sudoku.models import Board
from sudoku.solver import BacktrackSolver
from sudoku.validators import real_positive_number
from sudoku.utils import clear_screen
from sudoku.config import VERSION


_epilog = 'This program uses a backtracking algorithm. To learn more '  \
          'about backtracking and how it works, you can look at the '   \
          'built-in pydoc3 documentation and README.md file.'


def parse_arguments() -> ap.Namespace:
    parser = ap.ArgumentParser(
        description='A program to solve sudokus',
        formatter_class=ap.ArgumentDefaultsHelpFormatter,
        epilog=_epilog
    )
    parser.add_argument(
        '-g',
        '--grid',
        metavar='PATH',
        type=str,
        dest='filepath',
        help='file system path to text file containing a 9x9 '  \
             'sudoku grid, where empty entries are marked by '  \
             'any of the following symbols: {}'.format(Board.EMPTY_CHARS)
    )
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version='%(prog)s {}'.format(VERSION)
    )
    parser.add_argument(
        '-i',
        '--visualize',
        dest='visualize',
        action='store_true',
        help='shows a step-by-step run by re-drawing the board on ' \
             'each step'
    )
    parser.add_argument(
        '-d',
        '--delay',
        metavar='SECS',
        type=real_positive_number,
        dest='delay_secs',
        default=0.04,
        help='step delay, in seconds, when showing a step-by-step run'
    )
    parser.add_argument(
        '-b',
        '--benchmark',
        dest='benchmark',
        action='store_true',
        help='measure the time taken to solve a sudoku, in seconds ' \
             '(not recommended on step-by-step runs)'
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    board = Board(args.filepath)
    solver = BacktrackSolver(args)

    if args.visualize:
        clear_screen()
        print(str(board))
        print('Press <ENTER> to begin...')
        input()

    runtime = solver.solve(board)

    if not args.visualize:
        clear_screen()
        print(str(board))

    if args.benchmark:
        print(f'Solved in {runtime:.4f} secs')

    sys.exit(0)


if __name__ == '__main__':
    main()
