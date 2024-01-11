#!/usr/bin/env python3
"""safe_first_element function"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """function takes list and returns first element"""
    if lst:
        return lst[0]
    else:
        return None
