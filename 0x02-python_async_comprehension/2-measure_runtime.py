#!/usr/bin/env python3
"""measure runtime"""
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """function to measure runtime"""
    s: float = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    elapsed: float = time.perf_counter() - s

    return elapsed
