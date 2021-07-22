#!/usr/bin/env python3
# countasync.py
"""
Asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random
that waits for a random delay between 0 and max_delay
(included and float value) seconds and eventually returns it.
"""
import asyncio
import random


async def wait_random(max_delay: int=10) -> float:
    """
    The basics of async
    """
    i = random.randint(0, 10)
    await asyncio.sleep(i)
    return i
