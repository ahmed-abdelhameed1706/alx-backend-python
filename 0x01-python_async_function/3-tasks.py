#!/usr/bin/env python3
"""task 3 asyncio"""
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """function to return task"""
    return asyncio.create_task(wait_random(max_delay))
