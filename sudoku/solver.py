#!/usr/bin/env python3

'''Solvers are able to solve sudokus.

The solver currently available relies on a backtracking technique
for its solving algorithm.
'''

import argparse as ap

from typing import List, Tuple

from sudoku.models import Board
from sudoku.decorators import visualizer, benchmark


class BacktrackSolver:
    def __init__(self, args: ap.Namespace):
        self._solved = None

        if args.benchmark:
            self.solve = benchmark(self.solve)
        if args.visualize:
            self._backtrack = visualizer(self._backtrack, args.delay_secs)

    def solve(self, board: Board):
        self._solved = False
        moves = self._empty_positions(board)
        self._backtrack(board, moves, 0)

    def _backtrack(self, board: Board, moves: List[Tuple[int, int]], k: int):
        if self._is_solution(moves, k):
            self._solved = True
            return

        candidates = self._candidates(board, moves, k)
        for c in range(Board.MIN_VALUE, Board.MAX_VALUE + 1):
            if candidates[c]:
                self._add_entry(board, moves, k, c)
                self._backtrack(board, moves, k+1)
                if self._solved: break
                self._rem_entry(board, moves, k)

    def _is_solution(self, moves: List[Tuple[int, int]], k: int):
        return len(moves) == k

    def _candidates(self, board: Board, moves: List[Tuple[int, int]], k: int):
        clist = [False] + [True] * Board.ROW_ENTRIES
        i, j  = moves[k]
        row   = board.rows[i]
        col   = board.cols[j]
        reg   = board.region(i, j)

        # tag as unusable any candidate 'c' in the [1,9]
        # range that's already used in a row/col/region
        for c in range(Board.MIN_VALUE, Board.MAX_VALUE + 1):
            if c in row or c in col or c in reg:
                clist[c] = False

        return clist

    def _add_entry(self, board: Board, moves: List[Tuple[int, int]], k: int, c: int):
        i, j = moves[k]
        board[i, j] = c

    def _rem_entry(self, board: Board, moves: List[Tuple[int, int]], k: int):
        i, j = moves[k]
        board[i, j] = Board.EMPTY_ENTRY

    def _empty_positions(self, board: Board):
        return [
            (i, j)
            for i in range(Board.ROW_ENTRIES)
            for j in range(Board.COL_ENTRIES)
            if board[i, j] == Board.EMPTY_ENTRY
        ]
