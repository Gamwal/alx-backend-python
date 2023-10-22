#!/usr/bin/env python3
"""
Basic Annotations - sum_list
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    type-annotated function sum_list

    Args:
        n (float): number to find floor of

    Returns:
        sum of items in the list (float)
    """
    return sum(input_list)
