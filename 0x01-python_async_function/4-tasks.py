#!/usr/bin/env python3
"""task 2 of asyncio"""
import asyncio
from typing import List


task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """function that calls wait_random n times"""
    result: List[float] = []
    tasks: List = []

    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    for task in asyncio.as_completed(tasks):
        wait_time = await task
        result.append(wait_time)

    return result


n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))
