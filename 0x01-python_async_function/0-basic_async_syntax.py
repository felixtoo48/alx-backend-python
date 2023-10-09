#!/usr/bin/env python3
"""
asynchronous coroutine taking in an integer argument(max delay) with
default value of 10
named (wait_random) that awaits a delay between 0 and 10(max delay)
wait random value includes float values
"""
import asyncio
import time
from numpy import random


async def wait_random(max_delay=10):
    # Generate a random delay between 0 and max_delay seconds (inclusive).
    random_delay = random.uniform(0, max_delay)

    # wait for random delay
    await asyncio.sleep(random_delay)

    return random_delay
