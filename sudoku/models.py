#!/usr/bin/env python3

'''Models are are classes that encapsulate data.'''

from os import linesep
from typing import Text, Tuple

from sudoku.views import GridRowView, GridColumnView, GridRegionView


class InvalidBoardError(RuntimeError):
    pass


class InvalidEntryError(RuntimeError):
    pass


class Board:
    '''A sudoku board.'''
    ROW_ENTRIES = 9
    COL_ENTRIES = 9
    MAX_ENTRIES = ROW_ENTRIES * COL_ENTRIES
    EMPTY_ENTRY = 0
    EMPTY_CHARS = '-.0'
    EMPTY_CHAR = '.'
    MIN_VALUE = 1
    MAX_VALUE = 9

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
                try:
                    matrix.append([
                        Board.EMPTY_ENTRY if i in Board.EMPTY_CHARS else int(i)
                        for i in row[:-1]   # skip newline
                    ])
                except ValueError as e:
                    raise InvalidEntryError('entries must be in the [1,9] range')
        self._grid = matrix

    def _validate_grid(self):
        if len(self._grid) != Board.ROW_ENTRIES:
            raise InvalidBoardError(f'number of rows is not {Board.ROW_ENTRIES}')

        for row in self._grid:
            if len(row) != Board.COL_ENTRIES:
                raise InvalidBoardError(f'number of columns is not {Board.COL_ENTRIES}')

    def __getitem__(self, pos: Tuple[int, int]):
        i, j = pos
        return self._grid[i][j]

    def __setitem__(self, pos: Tuple[int, int], v: int):
        if v != Board.EMPTY_ENTRY and (v < Board.MIN_VALUE or v > Board.MAX_VALUE):
            raise InvalidEntryError(f'invalid entry: {v}')

        i, j = pos
        self._grid[i][j] = v

    def __str__(self):
        limit = 3   # entries per region per row/col
        line = '+---+---+---+' + linesep
        bar = '|'

        s = line
        g = self._grid
        for i in range(Board.ROW_ENTRIES):
            for j in range(Board.COL_ENTRIES):
                v  = str(g[i][j]) if g[i][j] != Board.EMPTY_ENTRY else Board.EMPTY_CHAR
                s += bar + v if j % limit == 0 else v
            s += bar + linesep
            if (i + 1) % limit == 0: s += line

        return s[:-1]   # remove newline
