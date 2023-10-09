#!/usr/bin/env python3
"""an asynchronous coroutine that takes 2 arguments"""
import random
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.
    Return a list of delays in ascending order.
    """
    delays = []

    async def wait_and_append_delay():
        delay = await wait_random(max_delay)
        delays.append(delay)

    tasks = [wait_and_append_delay() for _ in range(n)]
    await asyncio.gather(*tasks)

    return delays
