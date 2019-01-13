#!/usr/bin/env python3

'''
'''

import os

from collections import Sequence
from itertools import chain
from typing import Text, List, Tuple


class GridRowView(Sequence):
    def __init__(self, grid: List[List[int]]):
        self._grid = grid

    def __getitem__(self, i: int):
        return self._grid[i]

    def __len__(self):
        return len(self._grid)


class GridColumnView(Sequence):
    def __init__(self, grid: List[List[int]]):
        self._grid = grid

    def __getitem__(self, j: int):
        return [self._grid[i][j] for i in range(len(self._grid))]

    def __len__(self):
        return len(self._grid[0])


class GridRegionView(Sequence):
    # region index ranges
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

    def __init__(self, grid: List[List[int]], i: int, j: int):
        self._grid = grid
        self._rid  = self._get_region_id(i, j)

    def _get_region_id(self, i: int, j: int) -> int:
        # Get the set of possible regions where each
        # index (i, j) could be for the i-th row and
        # j-th column. The intersection of these two
        # sets is the actual region where the (i, j)
        # position is.
        r = self._row_regions_set(i)
        c = self._col_regions_set(j)
        return next(iter(r & c))

    def __getitem__(self, i: int):
        rows, cols = GridRegionView._RANGES[self._rid]
        i0, i1  = rows
        j0, j1  = cols
        # create a flat list (not sub-grid) for all
        # entries in the region, then return the i-th
        # element
        return list(
            chain(*[r[j0:j1] for r in self._grid[i0:i1]])
        )[i]

    def __len__(self):
        # a region is a flattened view of a 3x3 matrix
        return 9

    def _row_regions_set(self, i: int):
        a, b, c = {0, 1, 2}, {3, 4, 5}, {6, 7, 8}
        if i in a: return a
        if i in b: return b
        if i in c: return c
        return None

    def _col_regions_set(self, j: int):
        if j in (0, 1, 2): return {0, 3, 6}
        if j in (3, 4, 5): return {1, 4, 7}
        if j in (6, 7, 8): return {2, 5, 8}
        return None
