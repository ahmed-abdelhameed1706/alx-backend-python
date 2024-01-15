#!/usr/bin/env python3
"""asyn function"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> int:
    """function to await a number and return it"""
    await_number: float = random.uniform(0.0, float(max_delay))
    await asyncio.sleep(await_number)
    return await_number
