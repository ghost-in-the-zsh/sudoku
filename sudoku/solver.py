#!/usr/bin/env python3

'''
'''

import os

from typing import List, Tuple

from sudoku.models import Board


class BacktrackSolver:
    def __init__(self):
        self._solved = None

    def solve(self, board: Board):
        self._solved = False
        moves = self._analyze(board)
        self._backtrack(board, moves, 0)

    def _backtrack(self, board: Board, moves: List[Tuple[int, int]], k: int):
        if self._is_solution(moves, k):
            self._solved = True
            return

        candidates = self._candidates(board, moves, k)
        for c in range(1, len(candidates)):
            if candidates[c]:
                self._add_entry(board, moves, k, c)
                self._backtrack(board, moves, k+1)
                if self._solved: break
                self._rem_entry(board, moves, k)

    def _is_solution(self, moves: List[Tuple[int, int]], k: int):
        return len(moves) == k

    def _candidates(self, board: Board, moves: List[Tuple[int, int]], k: int):
        clist = [False] + [True] * Board.ROW_ENTRIES
        pos   = moves[k]
        i, j  = pos
        row   = board.rows[i]
        col   = board.cols[j]
        reg   = board.region(i, j)

        # tag as unusable any candidate 'c' in the [1,9]
        # range that's already used in a row/col/region
        for c in range(1, Board.ROW_ENTRIES + 1):
            if c in row or c in col or c in reg:
                clist[c] = False

        return clist

    def _add_entry(self, board: Board, moves: List[Tuple[int, int]], k: int, c: int):
        i, j = moves[k]
        board[i, j] = c

    def _rem_entry(self, board: Board, moves: List[Tuple[int, int]], k: int):
        i, j = moves[k]
        board[i, j] = Board.EMPTY_ENTRY

    def _analyze(self, board: Board):
        moves = []
        for i in range(len(board.rows)):
            for j in range(len(board.rows[i])):
                if board[i, j] == Board.EMPTY_ENTRY:
                    moves.append((i, j))
        return moves
