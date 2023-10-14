#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Asynchronous function that waits for a random amount of time

    Args:
        n (int): the number of times to spawn the function
        max_delay (int): the upper bound for the random number

    Returns:
        lst (list): list containing the delays for each call
    """

    results = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(results)
