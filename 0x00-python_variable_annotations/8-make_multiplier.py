#!/usr/bin/env python3
"""make multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function to return another multiplier function"""

    def multiplier_function(n: float) -> float:
        """multiplier function takes float and returns float"""
        return n * multiplier

    return multiplier_function
