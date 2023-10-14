#!/usr/bin/env python3
"""
Function to create Tasks
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Asynchronous function that waits for a random amount of time

    Args:
        n (int): the number of times to spawn the function
        max_delay (int): the upper bound for the random number

    Returns:
        results (list): sorted list containing the delays for each call
    """

    results = await asyncio.gather(*(task_wait_random(max_delay)
                                     for _ in range(n)))
    return sorted(results)
