#!/usr/bin/env python3
"""element_length function"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function takes list of sequences and returns list of tuples"""
    return [(i, len(i)) for i in lst]
