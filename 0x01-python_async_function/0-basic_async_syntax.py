#!/usr/bin/env python3
"""asyn function"""
import asyncio
import random


async def wait_random(max_delay=10):
    """function to await a number and return it"""
    await_number = random.uniform(0, 10)
    await asyncio.sleep(await_number)
    return await_number
