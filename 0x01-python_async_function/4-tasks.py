#!/usr/bin/env python3
# countasync.py
"""
Take the code from wait_n and alter it into a new
function task_wait_n. The code is nearly identical
to wait_n except task_wait_random is being called.
"""
import asyncio
import random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Task
    """
    list_del = []
    sp = []
    for i in range(n):
        list_del.append(task_wait_random(max_delay))
    for d in asyncio.as_completed(list_del):
        result = await d
        sp.append(result)
    return sp
