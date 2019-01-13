#!/usr/bin/env python3

'''
'''

import os

from typing import Text, Tuple

from sudoku.views import GridRowView, GridColumnView, GridRegionView


class InvalidBoardError(RuntimeError):
    pass


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
        return GridRowView(self._grid)

    @property
    def cols(self):
        return GridColumnView(self._grid)

    def region(self, i: int, j: int):
        return GridRegionView(self._grid, i, j)

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
