#!/usr/bin/env python3

'''
'''

import os

from collections import Sequence
from itertools import chain
from typing import Text, Tuple


class InvalidBoardError(RuntimeError):
    pass


class RowView(Sequence):
    def __init__(self, grid):
        self._grid = grid

    def __getitem__(self, i: int):
        return self._grid[i]

    def __len__(self):
        return len(self._grid)


class ColView(Sequence):
    def __init__(self, grid):
        self._grid = grid

    def __getitem__(self, j: int):
        return [self._grid[i][j] for i in range(len(self._grid))]

    def __len__(self):
        return len(self._grid[0])


class RegionView(Sequence):
    _RANGES = (
        # row  ,  col
        ((0, 3), (0, 3)),   # top left
        ((0, 3), (3, 6)),   # top mid
        ((0, 3), (6, 9)),   # top right

        ((3, 6), (0, 3)),   # mid left
        ((3, 6), (3, 6)),   # mid mid
        ((3, 6), (6, 9)),   # mid right

        ((6, 9), (0, 3)),   # bot left
        ((6, 9), (3, 6)),   # bot mid
        ((6, 9), (6, 9))    # bot right
    )

    def __init__(self, grid, rid: int):
        self._grid = grid
        self._rid  = rid

    def __getitem__(self, i: int):
        rows, cols = RegionView._RANGES[self._rid]
        i0, i1  = rows
        j0, j1  = cols
        # create a flat list (not sub-grid) for all
        # entries in the region, then return the i-th
        # element
        return list(
            chain(*[r[j0:j1] for r in self._grid[i0:i1]])
        )[i]

    def __len__(self):
        # regions are 3x3 matrices
        return 9


class Board:
    '''A sudoku board.'''
    ROW_ENTRIES = 9
    COL_ENTRIES = 9
    MAX_ENTRIES = ROW_ENTRIES * COL_ENTRIES
    EMPTY_ENTRY = 0
    EMPTY_CHARS = '-.0'
    EMPTY_CHAR  = '.'
    MIN_VALUE   = 1
    MAX_VALUE   = 9

    def __init__(self, filepath: Text):
        self._grid = None
        self._load_from(filepath)
        self._validate_grid()

    @property
    def rows(self):
        return RowView(self._grid)

    @property
    def cols(self):
        return ColView(self._grid)

    def region(self, i: int, j: int):
        # Get the set of possible regions where each
        # index (i, j) could be for the i-th row and
        # j-th column. The intersection of these two
        # sets is the actual region where the (i, j)
        # position is.
        a = self._row_regions_set(i)
        b = self._col_regions_set(j)
        return RegionView(self._grid, next(iter(a & b)))

    def _row_regions_set(self, i: int):
        g = ({a for a in range(b, b+3)} for b in range(0, Board.ROW_ENTRIES, 3))
        for s in g:
            if i in s: return s
        return None

    def _col_regions_set(self, j: int):
        if j in (0, 1, 2): return {0, 3, 6}
        if j in (3, 4, 5): return {1, 4, 7}
        if j in (6, 7, 8): return {2, 5, 8}
        return None

    def _load_from(self, filepath: Text):
        matrix = []
        with open(filepath, 'r') as grid:
            for row in grid:
                matrix.append([
                    Board.EMPTY_ENTRY if i in Board.EMPTY_CHARS else int(i)
                    for i in row[:-1]   # skip newline
                ])
        self._grid = matrix

    def _validate_grid(self):
        if len(self._grid) != Board.ROW_ENTRIES:
            raise InvalidBoardError('grid row count is not {}'.format(Board.ROW_ENTRIES))

        for row in self._grid:
            if len(row) != Board.COL_ENTRIES:
                raise InvalidBoardError('grid col count is not {}'.format(Board.COL_ENTRIES))

    def __getitem__(self, pos: Tuple[int, int]):
        i, j = pos
        return self._grid[i][j]

    def __setitem__(self, pos: Tuple[int, int], v: int):
        if v != Board.EMPTY_ENTRY and (v < Board.MIN_VALUE or v > Board.MAX_VALUE):
            raise ValueError('invalid entry: {}'.format(str(v)))

        i, j = pos
        self._grid[i][j] = v

    def __str__(self):
        limit = 3
        line  = '+---+---+---+' + os.linesep
        bar   = '|'

        s = line
        for i in range(len(self._grid)):
            for j in range(len(self._grid[i])):
                v  = str(self._grid[i][j]) if self._grid[i][j] != Board.EMPTY_ENTRY else Board.EMPTY_CHAR
                s += bar + v if j % limit == 0 else v
            s += bar + os.linesep
            if (i+1) % limit == 0: s += line

        return s[:-1]   # remove newline
