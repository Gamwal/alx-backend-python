#!/usr/bin/env python3
"""The basics of async"""

import asyncio
import random


async def wait_random(max_delay=10):
    """
    asynchronous function that waits
    for a random amount of time

    Args:
        max_delay (int): the upper bound for the
                         random number

    Return:
        wait (float): random number between 0 and max_delay
    """

    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
