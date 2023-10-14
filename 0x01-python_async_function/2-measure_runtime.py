#!/usr/bin/env python3
"""
Function to measure the runtime in async program
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Function to calculate average runtime

    Args:
        n (int): the number of times to spawn the wait_n function
        max_delay (int): the upper bound a random number

    Returns:
        result (float): average runtime
    """

    async def surrogate(n, max_delay):
        """
        Function to run and asynchronous function

        Args:
            n (int): the number of times to spawn the wait_n function
            max_delay (int): the upper bound a random number

        Returns:
            ffloat (float): average runtime
        """

        start_time = time.time()
        await wait_n(n, max_delay)
        total_time = time.time() - start_time
        return total_time / n

    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(surrogate(n, max_delay))
    return result
