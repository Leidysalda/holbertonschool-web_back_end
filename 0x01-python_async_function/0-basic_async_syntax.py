#!/usr/bin/env python3
"""
Asynchronous coroutine that takes in an integer argument
"""
import asyncio
import random


async def wait_random(max_delay: int=10) -> float:
    """
    The basics of async
    """
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
