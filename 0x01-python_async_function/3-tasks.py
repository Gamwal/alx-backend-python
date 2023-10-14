#!/usr/bin/env python3
"""
Tasks
"""

import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Function that to return an asyncio.Task object

    Args:
        max_delay (int): variable to serve as upper bound for random number

    Returns:
        task (asyncio.Task): An asynchronous task object
    """

    task = asyncio.create_task(wait_random(max_delay))
    return (task)
