#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""
import asyncio
import time
from typing import Generator, List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure_runtime should measure the total runtime and
    return it.
    """
    task = []
    t_start = time.time()
    for i in range(4):
        task.append(asyncio.create_task(async_comprehension()))
    await asyncio.gather(*task)
    t_end = time.time()
    return t_end - t_start
