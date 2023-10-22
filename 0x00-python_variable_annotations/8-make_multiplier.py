#!/usr/bin/env python3
"""
Complex types - functions
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Complex types - functions

    Args:
        multiplier (float)

    Returns: Function
    """

    def new_func(num: float):
        """
        New function to be returned
        """
        return multiplier * num

    return new_func
