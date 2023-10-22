#!/usr/bin/env python3
"""
Complex types - string and int/float to tuple
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Complex types - string and int/float to tuple

    Args:
        k (str)
        v(int or float)

    Returns:
        sum of items in the list (float)
    """
    return (k, v*v)
