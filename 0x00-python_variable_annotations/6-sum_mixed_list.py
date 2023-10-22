#!/usr/bin/env python3
"""
Complex types - list of float
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Complex types - list of float

    Args:
        mxd_lst (List): list of integers and floats

    Returns:
        sum of items in the list (float)
    """
    return sum(mxd_lst)
