#!/usr/bin/env python3
"""measure runtime"""
import time
import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """function to measure runtime"""
    s = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    elapsed = time.perf_counter() - s

    return elapsed
