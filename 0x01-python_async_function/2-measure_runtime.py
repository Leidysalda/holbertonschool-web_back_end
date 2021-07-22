#!/usr/bin/env python3
# countasync.py
"""
Create a measure_time function with integers n and
max_delay as arguments that measures the total execution
time for wait_n(n, max_delay), and returns total_time / n.
Your function should return a float.
"""
import asyncio
import random
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Measure the runtime
    """
    t_start = time.time()
    asyncio.run(wait_n(n, max_delay))
    t_end = time.time()
    total_mess = t_end - t_start
    return total_mess / n
