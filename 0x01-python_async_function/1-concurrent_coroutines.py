#!/usr/bin/env python3
"""task 2 of asyncio"""
import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """function that calls wait_random n times"""
    result: List[float] = []
    tasks: List = []

    for _ in range(n):
        task: float = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    for task in asyncio.as_completed(tasks):
        wait_time = await task
        result.append(wait_time)

    return result
