#!/usr/bin/env python3
# countasync.py
"""
Write an asynchronous coroutine that takes in an integer
argument (max_delay, with a default value of 10) named
wait_random that waits for a random delay between 0 and
max_delay (included and float value) seconds and eventually
returns it.
"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int=10) -> List[float]:
    """
    The list of the delays should be in ascending order without
    using sort() because of concurrency.
    """
    list_del = []
    sp = []
    for i in range(n):
        list_del.append(wait_random(max_delay))
    for d in asyncio.as_completed(list_del):
        result = await d
        sp.append(result)
    return sp
