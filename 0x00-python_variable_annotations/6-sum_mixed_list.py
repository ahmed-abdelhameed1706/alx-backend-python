#!/usr/bin/env python3
"""mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum_mixed_list takes ints or floats and returns sum"""
    return sum(mxd_lst)
